import os

from pprint import pprint

import requests

from dotenv import load_dotenv


def main():
    load_dotenv()
    DVMN_TOKEN = os.getenv("DVMN_TOKEN")
    dvmn_reviews_url = "https://dvmn.org/api/long_polling/"

    headers = {
        "Authorization": f"Token {DVMN_TOKEN}",
    }

    while True:
        try:
            response = requests.get(
                dvmn_reviews_url, headers=headers, timeout=5
            )
            response.raise_for_status()

            pprint(response.json())
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            pass


if __name__ == "__main__":
    main()
