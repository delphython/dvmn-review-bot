import os

import requests
import telegram

from dotenv import load_dotenv


def get_dvmn_api_response(url, token, timestamp):
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

    dvmn_token = os.getenv("DVMN_TOKEN")
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    dvmn_reviews_url = "https://dvmn.org/api/long_polling/"
    timestamp = None

    bot = telegram.Bot(token=telegram_token)

    while True:
        try:
            dvmn_api_response = get_dvmn_api_response(
                dvmn_reviews_url, dvmn_token, timestamp
            )

            if dvmn_api_response["status"] == "timeout":
                timestamp = str(dvmn_api_response["timestamp_to_request"])

            if dvmn_api_response["status"] == "found":
                lesson_check_properties = dvmn_api_response["new_attempts"][0]
                lesson_title = lesson_check_properties["lesson_title"]
                lesson_result = (
                    "К сожалению, в работе нашлись ошибки."
                    if lesson_check_properties["is_negative"]
                    else "Преподаватель принял Вашу работу!"
                )
                lesson_url = lesson_check_properties["lesson_url"]

                message_text = (
                    f'У Вас проверили работу "{lesson_title}".\n'
                    + f"{lesson_result}\nСсылка на урок: {lesson_url}"
                )

                bot.send_message(text=message_text, chat_id=chat_id)

        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            pass


if __name__ == "__main__":
    main()
