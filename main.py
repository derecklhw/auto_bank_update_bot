import schedule
import time
from scraper import scraper, data_processing
from notifications import whatsapp

def main():
    # schedule.every().day.at("09:00").do(run_scraper_and_notify)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    run_scraper_and_notify()

def run_scraper_and_notify():
    try:
        url = ["https://www.myt.mu/sinformer/foreignexchange", "https://www.abcbanking.mu/treasury/daily-indicative-foreign-exchange-rates/"]
        scraped_data = scraper.run_scraper(url)
        processed_data = data_processing.process_data(scraped_data)
        
        whatsapp.send_message(processed_data)

    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()
