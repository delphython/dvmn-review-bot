# DVMN Review Telegram Bot

DVMN Review Telegram Bot sends notifications about the review of DVMN lessons.

## Prerequisites

Python3 should be already installed. Use `pip` to install dependencies:
```bash
pip install -r requirements.txt
```

## Installation
You have to set DVMN_TOKEN, TELEGRAM_TOKEN and CHAT_ID environment variables before using the script.

1. Create .env file in the project directory.
2. Visit [DVMN API page](https://dvmn.org/api/docs/) and copy your token to .env file:
```
DVMN_TOKEN="b12c2c0b00f946abba12345c781de3ff12345678"
```
3. Create the bot and get a token from Telegram, see [this tutorial](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token) for instructions. Copy your Telegram API token to .env file:
```
TELEGRAM_TOKEN="1234567890:AAHOoGbQZQripXSKTn1ZRmKf6g3-wwwwwww"
```
4. CHAT_ID is the user id of the Telegram user to send messages to him. Copy it to .env file:
```
CHAT_ID="123456789"
```

## Usage

Run python script:
```sh
python dvmnbot.py
```
Use Ctrl+C to interrupt the script.

## Deploy
For deploying on [Heroku](https://www.heroku.com) you should:
1. Login or register there.
2. Create a new app.
3. Connect GitHub repository.:
4. Create `Procfile` in the project root directory and add the text:
```
bot: python3 dvmnbot.py
```
5. Add DVMN_TOKEN, TELEGRAM_TOKEN and CHAT_ID environment variables in the Settings tab of the Heroku site. You should fill `Config Vars`.
6. Don't forget to renew the project repository on Heroku.

## Meta

Vitaly Klyukin — [@delphython](https://t.me/delphython) — [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
