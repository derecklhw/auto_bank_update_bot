import re
from datetime import datetime
from utils import logging

def process_data(scraped_data):
    print("Processing data...")
    
   # Configure the logger
    logging.configure_logger()

    result = []
    existing_logs = set()  # To store existing log entries
    
    # Read existing logs from the file
    with open('scraped_data.log', 'r') as log_file:
        for line in log_file:
            if 'Bank:' in line and 'Date:' in line and 'Value:' in line:
                bank_date_value = re.search(r'Bank: (.*?) \| Date: (.*?) \| Value: (.*?)$', line)
                if bank_date_value:
                    bank_name = bank_date_value.group(1)
                    date = bank_date_value.group(2)
                    value = bank_date_value.group(3)
                    existing_logs.add((bank_name, date, value))

    for data in scraped_data:
        url = data['url']
        value = data['value']
        date = None
        
        # Extract the bank name from the URL
        bank_name = re.search(r"//(?:www\.)?(.*?)/", url).group(1)
        bank_name = bank_name.capitalize()  # Optional: Capitalize the bank name
        
        # Process the date based on the source
        if 'date' in data:
            date_text = data['date']
            date_match = re.search(r'(\d{2}\.\d{2}.\d{4})', date_text)
            if date_match:
                date = datetime.strptime(date_match.group(1), '%d.%m.%Y').strftime('%Y-%m-%d')
            else:
                alt_date_match = re.search(r'(\d{2}-[A-Za-z]{3}-\d{4})', date_text)
                if alt_date_match:
                    alt_date = datetime.strptime(alt_date_match.group(1), '%d-%b-%Y')
                    date = alt_date.strftime('%Y-%m-%d')

        if (bank_name, date, value) not in existing_logs:
            logging.log_data(bank_name, date, value)
            result.append({
                "bank_name": bank_name,
                "date": date,
                "value": value
            })

            # Add the new log entry to the existing logs set
            existing_logs.add((bank_name, date, value))
   
    return result