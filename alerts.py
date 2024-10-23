import requests

def send_telegram_alert(message):
    telegram_bot_token = "your_telegram_bot_token"
    chat_id = "your_chat_id"
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, data=data)
