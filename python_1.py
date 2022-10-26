from telethon import TelegramClient, events, sync, functions, types
from telethon.errors import rpcbaseerrors
from time import sleep
import fayl.animrun
import fayl.loverun
import fayl.smilerun
import fayl.iloverun
import fayl.loveemojirun
import fayl.moonrun
import fayl.bombrun
import fayl.fuckrun
import fayl.snowrun
import fayl.lovelyrun

import fayl.client,fayl.help


client = fayl.client.client
botClient = fayl.client.botClient
@client.on(events.NewMessage(pattern=".test"))
async def _(event):
    await event.reply("account ga muvafaqiyatli kira oldim")

with client as darknetos:
	 darknetos.add_event_handler(fayl.help.help)
with client as darknet:
	darknet.add_event_handler(fayl.animrun.animhandler)
with client as dark:
    dark.add_event_handler(fayl.loverun.lovehandler)
with client as smile:
    smile.add_event_handler(fayl.smilerun.smilehandler)
with client as ilove:
    ilove.add_event_handler(fayl.iloverun.ilovehandler)
with client as loveemoji:
    loveemoji.add_event_handler(fayl.loveemojirun.loveemojihandler)
with client as moon:
    moon.add_event_handler(fayl.moonrun.moonhandler)
with client as bomb:
    bomb.add_event_handler(fayl.bombrun.bombhandler)
with client as fuck:
    fuck.add_event_handler(fayl.fuckrun.fuckhandler)
with client as snow:
    snow.add_event_handler(fayl.snowrun.snowhandler)
with client as lovely:
    lovely.add_event_handler(fayl.lovelyrun.lovelyhandler)

client.start()
client.run_until_disconnected()