from telethon import TelegramClient, events
from fayl.fuck import Online
import time
fuck = Online()
@events.register(events.NewMessage)
async def fuckhandler(event):
	        if ".fuck" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in fuck.online:
	        		time.sleep(0.3)
	        		await event.edit(d)