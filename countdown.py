print('==========start==========')
import os
import sys
import asyncio
import datetime
from pyrogram import Client,filters, errors
from pyrogram.types import Message


#QQ before we start
app = Client("BillyKaiChengBot",api_id="17817209",api_hash=os.environ['API'],bot_token=os.environ['TOKEN'])
try:
    with app:
        app.send_message(-1001518766606, "#login\ndevice: [server](https://replit.com/@lmjaedentai/billy-telegram#main.py)", disable_web_page_preview=True,disable_notification=True,reply_markup=ReplyKeyboardRemove(),reply_to_message_id=179723)
        print('==========login==========')
except errors.exceptions.not_acceptable_406.AuthKeyDuplicated:
    os.remove("verypigbot.session")
    sys.exit('[shutdown] session file error')

#QQ user code
async def sleep_until(hour: int, minute: int, second: int):
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, t.day, hour, minute, second)
    if t.timestamp() > future.timestamp():
        future += datetime.timedelta(days=1)
    await asyncio.sleep((future - t).total_seconds())

def sendcountdown():
    difference = datetime.datetime(2024, 1, 30) - datetime.datetime.now()
    return difference.days+1

async def main():
    async with app:
        while True:
            await app.send_message(-1001197820173, f"**SPM**\n{sendcountdown()} days left")
            await sleep_until(12,21,0)
            
app.run(main())