import re
from datetime import datetime

def process_data(scraped_data):
    print("Processing data...")
    
    result = []

    for url, value in scraped_data.items():
        # Extract the bank name from the URL
        bank_name = re.search(r"//(?:www\.)?(.*?)/", url).group(1)
        bank_name = bank_name.capitalize()  # Optional: Capitalize the bank name
        
        # Create a readable format with bank name and value
        formatted_data = f"{bank_name}: {value}"
        result.append(formatted_data)
    
    result_string = '\n'.join(result)

    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime("%Y-%m-%d")

    # Add today's date to the result string
    result_string = f"{today_date}\n{result_string}"

    return result_string