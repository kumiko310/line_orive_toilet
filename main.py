import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open("info.json","r")
info = json.load(file)

CHANNEL_ACCESS_TOKEN=info['CHANNEL_ACCESS_TOKEN']
line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID=info['USER_ID']
    messages=TextSendMessage("そろそろ汚れてきたので、トイレのお掃除をお願いします🐈‍⬛")
    line_bot_api.push_message(USER_ID,messages=messages)

if __name__ == "__main__":
    main()
