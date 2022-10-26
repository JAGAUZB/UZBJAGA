from telethon import TelegramClient, events
from fayl.lovely import Online
import time
lovely = Online()
@events.register(events.NewMessage)
async def lovelyhandler(event):
	        if ".magiclovely" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in lovely.online:
	        		time.sleep(0.3)
	        		await event.edit(d)