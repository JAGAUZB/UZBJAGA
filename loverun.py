from telethon import TelegramClient, events
from fayl.love import Online
import time
love = Online()
@events.register(events.NewMessage)
async def lovehandler(event):
	        if ".love" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in love.online:
	        		time.sleep(0.3)
	        		await event.edit(d)