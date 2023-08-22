import schedule
import time
import yaml
from yaml import Loader
from scraper import scraper, data_processing
from notifications import whatsapp

def main():
    stream = open("config/config.yaml", 'r')
    config = yaml.load(stream, Loader=Loader)
    # schedule.every().day.at("09:00").do(run_scraper_and_notify)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    run_scraper_and_notify(config)

def run_scraper_and_notify(config):
    try:
        url = config.get('urls')
        country_list = config.get('country-list')
        phone_number = config.get('phone-number')
        scraped_data = scraper.run_scraper(url, country_list)
        processed_data = data_processing.process_data(scraped_data)
        
        whatsapp.send_message(processed_data, phone_number)

    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()
