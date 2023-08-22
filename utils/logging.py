
import logging

def configure_logger():
    # Configure the logging system
    logging.basicConfig(filename='scraped_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_data(url, date, country, value):
    logging.info(f"Url: {url} | Date: {date} | Country: {country} | Value: {value}")
