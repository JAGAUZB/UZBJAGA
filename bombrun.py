from telethon import TelegramClient, events
from fayl.bomb import Online
import time
bomb = Online()
@events.register(events.NewMessage)
async def bombhandler(event):
	        if ".boom" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in bomb.online:
	        		time.sleep(0.3)
	        		await event.edit(d)