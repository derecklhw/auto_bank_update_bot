# AutoBankUpdateBot

This Python project is designed to scrape data from specified URLs, process the data, and send notifications via WhatsApp. It is a versatile tool that can be configured to monitor and notify you about various data sources.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x is installed on your system.
- You have created a virtual environment for this project (optional but recommended).

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/derecklhw/auto_bank_update_bot.git
   ```

2. Navigate to the project directory:

   ```sh
   cd auto_bank_update_bot
   ```

3. Install the required dependencies listed in requirements.txt:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Configuration

Copy `config.yaml.example` to `config.yaml` and fill in the necessary configuration details:

- phone-number: Target WhatsApp phone number.
- urls: A list of URLs to scrape data from.
- country-list: A list of countries currency to filter data by.

### Running the Scraper

To run the data scraper and notification system, execute the following command:

```sh
python main.py
```

You can schedule this script to run periodically, e.g., daily at a specific time, using a task scheduler like Cron (Linux)
