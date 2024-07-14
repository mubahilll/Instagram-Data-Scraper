import os
import requests
import json
import time
from dotenv import load_dotenv
# Team ETA Banner


# Constants
 

KEYWORDS = ['vibin', 'farewell']
HASHTAGS = ['#cybersecurity', '#hacking']

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


load_dotenv()


def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to get user details
def get_user_details(user_id, access_token, count):
    print(f"\n[{count}] Processing user {user_id}...")
    url = f'https://graph.instagram.com/{user_id}?fields=id,username,media_count,account_type&access_token={access_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{RED}[X] Error making user api request for {user_id}{RESET}")
        return None

# Function to get user's media details
def get_user_media(user_id, access_token):
    media_url = f'https://graph.instagram.com/{user_id}/media?fields=id,caption,media_type,media_url,timestamp,permalink,thumbnail_url&access_token={access_token}'
    response = requests.get(media_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{RED}[X] Error making media api request for {user_id}{RESET}")
        return None

# Function to monitor and collect posts containing specific keywords or hashtags
def keyword_hashtag_monitoring(media_data, keywords, hashtags):
    monitored_posts = []
    for post in media_data.get('data', []):
        caption = post.get('caption', '').lower()
        if any(keyword in caption for keyword in keywords) or any(hashtag in caption for hashtag in hashtags):
            monitored_posts.append(post)
    return monitored_posts

# Rate limiting
def rate_limit_handling():
    print("\nSleeping for 2 seconds...")
    time.sleep(2)

# Main function to run the scraper
def main():
    count = 1
    users_json = os.getenv('USERS')
    # print(users_json)
    users = json.loads(users_json)

    for user_id, access_token in users.items():

        user_data = get_user_details(user_id, access_token, count)
        count += 1

        if user_data:
            print(f"{GREEN}[+] User Data: {YELLOW}{user_data}{RESET}")

        media_data = get_user_media(user_id, access_token)
        if media_data:
            if user_data['media_count'] == 0:
                print(f"{RED}[X] No media found{RESET}")
            else:
                SAVE_DIR = f"{os.getenv('SAVE_DIR')}/{user_data['username']}"
                ensure_directory(SAVE_DIR)

                # Save media data to JSON file
                media_file_path = os.path.join(SAVE_DIR, f"{user_data['username']}_media.json")
                with open(media_file_path, 'w') as file:
                    json.dump(media_data, file, indent=4)
                print(f"{GREEN}[+] Media data saved to {media_file_path} {RESET}")

                # Monitor and collect posts containing specific keywords or hashtags
                monitored_posts = keyword_hashtag_monitoring(media_data, KEYWORDS, HASHTAGS)
                if monitored_posts:
                    monitored_posts_file_path = os.path.join(SAVE_DIR, f"{user_data['username']}_monitored_posts.json")
                    with open(monitored_posts_file_path, 'w') as file:
                        json.dump(monitored_posts, file, indent=4)
                    print(f"{GREEN}[+] Monitored posts saved to {monitored_posts_file_path}{RESET}")
                else:
                    print(f"{RED}[X] No posts found with specified keywords or hashtags.{RESET}")

        # Implement rate limiting
        rate_limit_handling()
        

if __name__ == "__main__":
    main()
