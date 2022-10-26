from telethon import TelegramClient, events
from fayl.smile import Online
import time
smile = Online()
@events.register(events.NewMessage)
async def smilehandler(event):
	        if ".smile" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in smile.online:
	        		time.sleep(0.3)
	        		await event.edit(d)