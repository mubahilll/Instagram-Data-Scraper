# Instagram Data Scraper

This project contains two main scripts: `access_token.py` for obtaining an Instagram access token and `insta_scrapper.py` for scraping Instagram data based on specific keywords and hashtags.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Notes](#notes)
- [License](#license)

## Introduction

The Instagram Data Scraper is designed to help you authenticate with Instagram's API, obtain an access token, and then scrape user data and media posts based on specific keywords and hashtags.

## Features

- Obtain both short-lived and long-lived Instagram access tokens.
- Scrape user details and media posts.
- Monitor and collect posts containing specific keywords or hashtags.
- Save the scraped data to JSON files.

## Requirements

- Python 3.x
- The following Python packages:
  - `requests`
  - `webbrowser`
  - `python-dotenv`

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/instagram-data-scraper.git
    cd instagram-data-scraper
    ```

2. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Create a `.env` file** in the root directory and add your Instagram API credentials:

    ```env
    client_id=YOUR_INSTAGRAM_CLIENT_ID
    client_secret=YOUR_INSTAGRAM_CLIENT_SECRET
    redirect_uri=YOUR_REDIRECT_URI
    SAVE_DIR=./scraped_data
    USERS={"user_id1": "access_token1", "user_id2": "access_token2"}
    ```

## Usage

### Step 1: Obtain Access Token

1. Run `access_token.py` to start the authentication process and obtain an access token.

    ```sh
    python access_token.py
    ```

2. Follow the prompts to log in to Instagram and authorize the application. Paste the redirected URL back into the script when prompted.

3. The script will output a long-lived access token that you can use in the `insta_scrapper.py` script.

### Step 2: Scrape Instagram Data

1. Update the `USERS` variable in your `.env` file with the user IDs and access tokens obtained from the previous step.

2. Run `insta_scrapper.py` to start scraping data.

    ```sh
    python insta_scrapper.py
    ```

3. The script will save user details, media data, and monitored posts (based on specified keywords and hashtags) to JSON files in the directory specified by `SAVE_DIR`.

## Notes

- Ensure you comply with Instagram's API usage policies.
- The current implementation handles rate limiting by sleeping for 2 seconds between requests.
- Customize the `KEYWORDS` and `HASHTAGS` lists in `insta_scrapper.py` as per your needs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
