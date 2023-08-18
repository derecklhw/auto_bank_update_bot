import requests
from bs4 import BeautifulSoup

def run_scraper(urls):
    values = {}
    for url in urls:
        print("Processing URL:", url)
        # Perform a GET request to fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the table element with class "daily-forex-table"
        target_table = soup.find("table")

        if target_table:
            # Find all rows in the table
            rows = target_table.find_all("tr")

            for row in rows:
                # Find all columns in the row
                columns = row.find_all("td")

                # Check if the row contains "Canada"
                if any("canada" in col.get_text().lower() for col in columns):
                    # Get the last column value
                    last_column_value = columns[-1].get_text().strip()
                    values.update({url: last_column_value})
                    print("Found 'Canada' in row. Selling:", last_column_value)

    if values:
        return values
    else:
        return "Canada not found in any row."