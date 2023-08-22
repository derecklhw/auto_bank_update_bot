
import logging

def configure_logger():
    # Configure the logging system
    logging.basicConfig(filename='scraped_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_data(bank_name, date, currency, value):
    logging.info(f"Url: {bank_name} | Date: {date} | Currency: {currency} | Value: {value}")
