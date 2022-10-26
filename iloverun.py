from telethon import TelegramClient, events
from fayl.ilove import Online
import time
ilove = Online()
@events.register(events.NewMessage)
async def ilovehandler(event):
	        if ".ilove" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in ilove.online:
	        		time.sleep(0.3)
	        		await event.edit(d)