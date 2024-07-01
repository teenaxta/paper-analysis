# Conference Paper Scraper

This project is designed to scrape conference paper authors and titles based on specified conferences and years. It outputs the results into CSV files for further analysis or record-keeping.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python
- pip for installing Python packages

### Installation

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/yourusername/conference-paper-scraper.git
   cd conference-paper-scraper
   ```

2. Make environment and instal requirements
   ```sh
   python -m venv .env
   source .env/bin/activate
   pip install -r requirements.txt
   ```

3. Add the needed conferences in conferences/conferences.txt and years in conferences/years.txt

4. Run it using 
   ```sh
   python main.py -c "conferences/conferences.txt" -y "conferences/years.txt" -m '1'
   ```
-m 100s of papers