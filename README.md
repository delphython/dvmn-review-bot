# DVMN Review Telegram Bot

DVMN Review Telegram Bot sends notifications about the review of DVMN lessons.

## Prerequisites

Python3 should be already installed. Use `pip` to install dependencies:
```bash
pip install -r requirements.txt
```

Install docker based on your operating system.
For ubuntu 18.04:
```bash
apt-get update
apt-get install ca-certificates curl gnupg lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update
apt-get install docker-ce docker-ce-cli containerd.io docker-compose
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

Build the docker image:
```sh
docker build --tag dvmn-review-bot .
```

Run your container in detached mode or in the background:
```sh
docker run -d dvmn-review-bot
```

To restart your container:
```sh
docker restart dvmn-review-bot
```

To stop your container (stop the bot):
```sh
docker stop dvmn-review-bot
```

## Deploy
For deploying on [Heroku](https://www.heroku.com) you should:
1. Login or register there.
2. Open [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
3. Login to Heroku:
```sh
heroku login
```
4. Create your app:
```
heroku create my-app-name --manifest
```
5. Clone repository:
```
git clone https://github.com/yourgithublogin/yourrepo.git
```
6. Push your app to Heroku:
```
git push heroku main
```


## Meta

Vitaly Klyukin — [@delphython](https://t.me/delphython) — [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
