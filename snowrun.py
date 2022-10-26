from telethon import TelegramClient, events
from fayl.snow import Online
import time
snow = Online()
@events.register(events.NewMessage)
async def snowhandler(event):
	        if ".snow" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in snow.online:
	        		time.sleep(0.3)
	        		await event.edit(d)