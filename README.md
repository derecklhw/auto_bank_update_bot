# AutoBankUpdateBot

This Python project is designed to scrape forex selling price data from specified bank URLs, process the data, and send notifications via WhatsApp. It is a versatile tool that can be configured to monitor and notify you about various data sources.

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

### Scheduling the Script

You can automate the execution of the script by scheduling it to run at specific times using a task scheduler like `Cron` or `systemd/timer` **(Linux/macOS)** or `Task Scheduler` **(Windows)**.

Here's an example of scheduling the script to run every 15 minutes between 9:00 AM and 10:00 AM daily using `Cron` on Linux or macOS:

```sh
*/15 9 * * * /path/to/python /path/to/main.py
```

Make sure to replace `/usr/bin/python3` with the **actual path to your Python interpreter** and `/path/to/main.py` with the full path to your main.py script.
