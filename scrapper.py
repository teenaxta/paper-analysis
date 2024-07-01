import requests
import csv


def get_conference_authors(search_query, max_papers):
    # Initialize an empty list to store the paper titles
    paper_titles = []
    authors = []

    # Perform the search and retrieve the paper titles
    start = 0
    print("HERE")
    # Construct the API request URL
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={search_query}&offset={start}&limit=100&fields=title,authors"
    
    # Make the API request
    response = requests.get(url)
    
    try:
        # Extract the paper titles from the response
        data = response.json()
        for paper in data["data"]:
            paper_authors = ", ".join([author['name'] for author in paper['authors']])
            print(paper_authors)
            authors.append(paper_authors)
            paper_titles.append(paper["title"])
        
        # Update the start offset for the next request
    except Exception as e:
        # Handle the error case
        print(f"Error: {response.status_code} - {response.text}")

    start += 100
    
    return authors, paper_titles

def get_all_authors(conferences, years, max_papers):
    
    for conference in conferences:
        for year in years:
            search_query = f"{conference} {year}"
            authors, paper_titles = get_conference_authors(search_query, max_papers)
            # Create a CSV file to store the authors and titles

            filename = f"results/{conference}_{year}.csv"
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Author", "Title"])  # Write the header row

                # Write the authors and titles to the CSV file
                for i in range(len(authors)):
                    writer.writerow([authors[i], paper_titles[i]])

if __name__ == "__main__":
    # Define the target conferences, years, and maximum number of papers to retrieve
    conferences = ["Computer Vision and Pattern Recognition"]
    years = ["2023"]
    max_papers = 1

    # Retrieve the authors and paper titles for the specified conferences and years
    get_all_authors(conferences, years, max_papers)