import os

import requests

from dotenv import load_dotenv


def main():
    load_dotenv()
    DVMN_TOKEN = os.getenv("DVMN_TOKEN")
    dvmn_reviews_url = "https://dvmn.org/api/user_reviews/"

    headers = {
        "Authorization": f"Token {DVMN_TOKEN}",
    }

    response = requests.get(dvmn_reviews_url, headers=headers)
    response.raise_for_status()


if __name__ == "__main__":
    main()
