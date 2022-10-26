from telethon import TelegramClient, events
from fayl.loveemoji import Online
import time
loveemoji = Online()
@events.register(events.NewMessage)
async def loveemojihandler(event):
	        if ".emojilove" in event.raw_text:
	        	time.sleep(0.3)
	        	for d in loveemoji.online:
	        		time.sleep(0.3)
	        		await event.edit(d)