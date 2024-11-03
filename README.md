# AutoBankUpdateBot

Designed to scrape forex selling price data from specified bank URLs and send the data as notifications via WhatsApp.

## Getting Started

### Prerequisites

- Python 3.x.
- A virtual environment.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/derecklhw/auto_bank_update_bot.git
   ```

2. Navigate to the project directory:

   ```sh
   cd auto_bank_update_bot
   ```

3. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

4. Install the required dependencies listed in requirements.txt:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Configuration

1. Make a copy of `config.yaml.example` to `config.yaml`.

   ```sh
   cp config.yaml.example config.yaml`
   ```

3. Fill in the necessary configuration details:

- phone-number: Target WhatsApp phone number.
- urls: A list of URLs to scrape data from.
- country-list: A list of countries currency to filter data by.

### Activate Virtual Environment

```sh
source venv/bin/activate
```

### Run

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
