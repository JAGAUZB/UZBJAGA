from telethon import TelegramClient, events, sync, functions, types, Button

import fayl.client
client = fayl.client.client
botClient = fayl.client.botClient
@botClient.on(events.InlineQuery)
async def _(query):
	      if query.text == "help":
	      	result = query.builder.article('Help', text = "~~JAGA ANONYMOUS, CLUB~~", buttons= [
	      	[Button.inline("A.N.O.N.Y.M.O.U.S", data=b"1")]
	      	
	      	])
	      	await query.answer([result])
@botClient.on(events.CallbackQuery)
async def uzgaruvchi(event):
	     
	     if event.data==b'1':
	          await event.answer("J.A.G.A USERBOT", alert=True)
@events.register(events.NewMessage(pattern=".help"))
async def help(event):
	    result = await client.inline_query("@UzbAloqabot_bot", "help")
	    await result[0].click(event.chat_id)
	    await event.message.delete()