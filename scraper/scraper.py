import requests
from bs4 import BeautifulSoup

def run_scraper(url):
    # URL of the bank's website page to scrape

    # Perform a GET request to fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table element with class "daily-forex-table"
    target_table = soup.find("table", class_="daily-forex-table")

    if target_table:
        return target_table
    else:
        return "Table not found with class 'daily-forex-table'."
