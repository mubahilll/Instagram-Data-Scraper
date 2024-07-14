# Instagram Data Scraper

This project contains two main scripts: `access_token.py` for obtaining an Instagram access token and `insta_scrapper.py` for scraping Instagram data based on specific keywords and hashtags.


### Prerequisites

1. **Python 3.x** installed on your system.
2. **Facebook Developer Account** to create and manage your Instagram app.

### Step-by-Step Setup

### Step 1: Setting Up the Instagram App

1. **Create a Facebook Developer Account** if you don't have one already: [Facebook Developer](https://developers.facebook.com/).
2. **Create a New App:**
    - Navigate to the [App Dashboard](https://developers.facebook.com/apps/).
    - Click on the "Create App" button.
    - Choose "For Everything Else" and click "Next".
    - Provide a Display Name for your app and your email, then click "Create App ID".
3. **Add Instagram Basic Display:**
    - In your app dashboard, click on "Set Up" under the Instagram Basic Display product.
    - Follow the instructions to create an Instagram Test User.
4. **Configure Instagram Basic Display:**
    - Go to the "Settings" -> "Basic" in your app dashboard.
    - Scroll down to the "Add Platform" section and select "Website".
    - Enter your website's URL in the "Site URL" field or in case you don’t have any, you can set a website on Github. (e.g., `https://abc.github.io/`).
5. **Add Valid OAuth Redirect URIs:**
    - In the same "Settings" -> "Basic" section, scroll down to "Valid OAuth Redirect URIs".
    - Enter the redirect URI: `https://ab.github.io/`.
6. **Get Your Instagram App Credentials:**
    - Note down your `App ID` and `App Secret` from the "Settings" -> "Basic" section.

### Step 2: Setting Up the Project Locally

1. **Clone the Repository:**
    
    ```bash
    git clone https://github.com/mubahilll/instagram-data-scraper.git
    cd instagram-data-scraper
    ```
    
2. **Install Required Packages:**
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Create a `.env` File:**
    
    In the root directory of your project, create a `.env` file and add your Instagram app credentials and other necessary variables:
    
    ```python
    client_id=YOUR_INSTAGRAM_CLIENT_ID
    client_secret=YOUR_INSTAGRAM_CLIENT_SECRET
    redirect_uri=YOUR_REDIRECT_URI
    SAVE_DIR=./scraped_data
    USERS={"user_id1": "access_token1", "user_id2": "access_token2"}
    ```
    
    Replace `YOUR_INSTAGRAM_CLIENT_ID`, `YOUR_INSTAGRAM_CLIENT_SECRET`, and `YOUR_REDIRECT_URI` with the appropriate values from your Instagram app setup.
    

### Step 3: Obtaining the Access Token

1. **Run `access_token.py`:**
    
    ```bash
    python access_token.py
    ```
    
2. **Follow the Prompts:**
    - The script will open a browser window for you to log in to Instagram and authorize the application.
    - After logging in, you will be redirected to your specified redirect URI. Copy the full redirected URL.
    - Paste the redirected URL back into the script when prompted.
3. **Get the Long-Lived Access Token:**
    - The script will output a long-lived access token which you can use for subsequent API requests.

### Step 4: Scraping Instagram Data

1. **Update the `USERS` Variable:**
    
    Update the `USERS` variable in your `.env` file with the user IDs and access tokens obtained from the previous step.
    
2. **Run `insta_scrapper.py`:**
    
    ```bash
    python insta_scrapper.py
    ```
    
3. **Scrape Data:**
    - The script will fetch user details and media posts, and save the data to JSON files in the directory specified by `SAVE_DIR`.
    - It will also monitor and collect posts containing specific keywords or hashtags.

### Notes

- Ensure you comply with Instagram's API usage policies.
- The current implementation handles rate limiting by sleeping for 2 seconds between requests.
- Customize the `KEYWORDS` and `HASHTAGS` lists in `insta_scrapper.py` as per your needs.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
