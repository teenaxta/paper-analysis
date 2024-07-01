import argparse
from scrapper import get_all_authors

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--confernces', '-c', type=str, help='Target Conferences Path')
    parser.add_argument('--years','-y', type=str, help='Target Conference Years Path')
    parser.add_argument('--max_papers','-m', type=int, help='Maximum number of papers to retrieve')
    args = parser.parse_args()


    print(args.confernces)

    # Define the target conferences, years, and maximum number of papers to retrieve
    # Read conference names from the txt file
    with open(args.confernces, 'r') as file:
        target_conferences = file.read().splitlines()
    
    with open(args.years, 'r') as file:
        target_years = file.read().splitlines()

    # Define the target conferences, years, and maximum number of papers to retrieve
    max_papers = args.max_papers

    # Call the function to get all authors
    get_all_authors(target_conferences, target_years, max_papers)
    

if __name__ == "__main__":
    main()