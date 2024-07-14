import requests
import webbrowser
import time
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1: Open the authorization URL in a browser
client_id = os.getenv('client_id')
redirect_uri = os.getenv('redirect_uri')
scope = 'user_profile,user_media'
response_type = 'code'

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

auth_url = f'https://api.instagram.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type={response_type}'

print(f"{GREEN}[+] Opening the browser for authorization...{RESET}")
webbrowser.open(auth_url)

# Step 2: Wait for the user to log in and get the redirected URL
redirected_url = input(f"{YELLOW}[+] Paste the full redirected URL here: {RESET}")

# Step 3: Extract the authorization code from the redirected URL
parsed_url = urlparse(redirected_url)
auth_code = parse_qs(parsed_url.query).get('code', [None])[0]

if auth_code and auth_code.endswith('#_'):
    auth_code = auth_code[:-2]

if not auth_code:
    print(f"{RED}[X] Failed to obtain authorization code.{RESET}")
else:
    # Step 4: Exchange the authorization code for a short-lived access token
    client_secret = os.getenv('client_secret')

    token_url = 'https://api.instagram.com/oauth/access_token'
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
        'code': auth_code
    }

    response = requests.post(token_url, data=payload)
    access_token_info = response.json()

    if 'access_token' in access_token_info and 'user_id' in access_token_info:
        short_lived_access_token = access_token_info['access_token']
        user_id = access_token_info['user_id']

        # Step 5: Exchange the short-lived access token for a long-lived access token
        long_lived_token_url = 'https://graph.instagram.com/access_token'
        params = {
            'grant_type': 'ig_exchange_token',
            'client_secret': client_secret,
            'access_token': short_lived_access_token
        }

        long_lived_response = requests.get(long_lived_token_url, params=params)
        long_lived_token_info = long_lived_response.json()

        if 'access_token' in long_lived_token_info:
            long_lived_access_token = long_lived_token_info['access_token']
            print(f"\n{GREEN}[+] Authorization successful!{RESET}")
            print(f"[+] Printing User_ID:Access_Token...")
            time.sleep(1)
            print(f"{YELLOW}'{user_id}':'{long_lived_access_token}'{RESET}")
        else:
            print(f"{RED}[X] Failed to obtain long-lived access token.{RESET}")
            print(f"{RED}Response: {long_lived_token_info}{RESET}")
    else:
        print(f"{RED}[X] Failed to obtain short-lived access token or user ID.{RESET}")
        print(f"{RED}Response: {access_token_info}{RESET}")
