import telepot
import urllib3
import requests
from app import settings

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

bot = telepot.Bot(settings.TELEGRAM_API_KEY)
bot.setWebhook("https://elkabelaya.pythonanywhere.com/telegrambot/{}".format(settings.TELEGRAM_SECRET_KEY), max_connections=1)


def telegram_webhook(json_data):
    respond_message = ""

    chat_id = json_data["message"]["chat"]["id"]
    text = json_data["message"]["text"]
    if text == "/start":
        respond_message = "Hi, {}, this is Bot".format(update["message"]["from"]["first_name"])
    elif text == "/video":
        respond_message = "https://rutube.ru/video/f84d877a28e806a2574cdf327fd05997/"
    elif text == "/usd":
        response = requests.get('https://www.cbr.ru/Queries/AjaxDataSource/112805?DT=&val_id=R01235')
        respond = response.json()
        respond_message = respond[4]["curs"]
    else:
        respond_message = "I do not know what you said: '{}'".format(text)

    bot.sendMessage(chat_id, respond_message)
