import logging
import os

from time import sleep

import requests
import telegram
import textwrap

from dotenv import load_dotenv


class TelegramLogsHandler(logging.Handler):
    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def get_dvmn_api_response(url, token, timestamp):
    headers = {
        "Authorization": f"Token {token}",
    }
    params = {
        "timestamp": timestamp,
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
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
    suspension_time = 60
    failed_connection_attempts = 0
    max_failed_connection_attempts = 5

    bot = telegram.Bot(token=telegram_token)

    logging.basicConfig(format="%(levelname)s %(message)s")
    logger = logging.getLogger("Бот логгер")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(bot, chat_id))

    logger.info("Бот запущен!")

    while True:
        try:
            dvmn_api_response = get_dvmn_api_response(
                dvmn_reviews_url, dvmn_token, timestamp
            )

            if dvmn_api_response["status"] == "timeout":
                timestamp = dvmn_api_response["timestamp_to_request"]

            if dvmn_api_response["status"] == "found":
                lesson_check_properties = dvmn_api_response["new_attempts"][0]
                lesson_title = lesson_check_properties["lesson_title"]
                lesson_result = (
                    "К сожалению, в работе нашлись ошибки."
                    if lesson_check_properties["is_negative"]
                    else "Преподаватель принял Вашу работу!"
                )
                lesson_url = lesson_check_properties["lesson_url"]

                message_text = textwrap.dedent(
                    f"""\
                    У Вас проверили работу "{lesson_title}".
                    {lesson_result}
                    Ссылка на урок: {lesson_url}
                    """
                )

                bot.send_message(text=message_text, chat_id=chat_id)

        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            failed_connection_attempts += 1
            if failed_connection_attempts == max_failed_connection_attempts:
                logger.warning(
                    "Exceeded the number of maximum connection attempts"
                )
                sleep(suspension_time)
                failed_connection_attempts = 0
        except Exception as e:
            logger.error(f"Бот упал с ошибкой: {e}")
            raise e


if __name__ == "__main__":
    main()
