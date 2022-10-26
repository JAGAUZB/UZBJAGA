from telethon import TelegramClient, events
from fayl.moon import Online
import time
moon = Online()
@events.register(events.NewMessage)
async def moonhandler(event):
	        if ".raining" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in moon.online:
	        		time.sleep(0.3)
	        		await event.edit(d)