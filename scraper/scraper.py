import requests
from bs4 import BeautifulSoup

def run_scraper(urls, country_list):
    values = []
    for url in urls:
        print("Processing URL:", url)
        # Perform a GET request to fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the table element with class "daily-forex-table"
        target_table = soup.find("table")

        target_date_html = soup.find("div", style="font-size:25px;font-weight:bold;")
        if target_date_html is None:
            target_date_html = soup.find("p", {"class": "timestamp"})
        
        target_date = target_date_html.get_text()

        if target_table:
            # Find all rows in the table
            rows = target_table.find_all("tr")

            for row in rows:
                # Find all columns in the row
                columns = row.find_all("td")

                for country in country_list:
                    # Check if the row contains country in country_list
                    if any(country in col.get_text().lower() for col in columns):
                        # Get the last column value
                        last_column_value = columns[-1].get_text().strip()
                        values.append({"url": url, "date": target_date,"country": country, "value": last_column_value})

    if values:
        return values