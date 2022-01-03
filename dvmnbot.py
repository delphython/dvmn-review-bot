import os

from pprint import pprint

import requests

from dotenv import load_dotenv


def get_dvmn_api_responce(url, token, timestamp):
    headers = {
        "Authorization": f"Token {token}",
        "timestamp": timestamp,
    }

    response = requests.get(
        url,
        headers=headers,
    )

    response.raise_for_status()

    return response.json()


def main():
    load_dotenv()

    DVMN_TOKEN = os.getenv("DVMN_TOKEN")
    dvmn_reviews_url = "https://dvmn.org/api/long_polling/"
    timestamp = None

    while True:
        try:
            dvmn_api_response = get_dvmn_api_responce(
                dvmn_reviews_url, DVMN_TOKEN, timestamp
            )
            if dvmn_api_response["status"] == "timeout":
                timestamp = str(dvmn_api_response["timestamp_to_request"])
            pprint(dvmn_api_response)
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            pass


if __name__ == "__main__":
    main()
