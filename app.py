from pyrogram import Client, filters
from pyrogram.types import Message
from DataBase import DB, AdminIDS, AllowedCHATS
from classes import Trigger_info
import config
bot = Client(
    name="session",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.TOKEN,
)
db=DB()
allowed_chats_db=AllowedCHATS()
admin_ids_db=AdminIDS()
OWNER_ID=850966027

async def chat_check(_, __, query: Message):
    return allowed_chats_db.find(query.chat.id)
async def admin_check(_, __, query: Message):
    return admin_ids_db.find(query.from_user.id)

@bot.on_message(filters.command(["add"]) &filters.create(admin_check)&filters.reply)
async def add_command(client: Client, message: Message):
    db.save(Trigger_info(message.text[5:].lower(), message.reply_to_message.text))
    await message.reply("Сохранил триггер")

@bot.on_message(filters.command(["del"]) &filters.create(admin_check)&filters.reply)
async def add_command(client: Client, message: Message):
    db.delete(message.reply_to_message.text.lower())
    await message.reply("Удалил триггер")

@bot.on_message(filters.command(["triggers"]))
async def add_command(client: Client, message: Message):
    a=db.find_all()
    if a:
        text='Список триггеров:\n'
        for row in a:
            text+=row.trigger+'\n'
        await client.send_message(chat_id=message.chat.id,reply_to_message_id=message.id,text=text, disable_web_page_preview=True)
    else:
        await message.reply("Не нашел триггеров")
@bot.on_message(filters.command(["add_admin"])& filters.reply)
async def add_admin_command(client: Client, message: Message):
    if message.from_user.id == OWNER_ID:
        if admin_ids_db.save(message.reply_to_message.from_user.id):
            await message.reply("Добавил админа!")
        else:
            await message.reply("Ошибка!")
@bot.on_message(filters.command(["del_admin"])& filters.reply)
async def add_admin_command(client: Client, message: Message):
    if message.from_user.id == OWNER_ID:
        if admin_ids_db.delete(message.reply_to_message.from_user.id):
            await message.reply("Удалил админа!")
        else:
            await message.reply("Ошибка!")

@bot.on_message(filters.command(["add_chat"]))
async def add_admin_command(client: Client, message: Message):
    if message.from_user.id == OWNER_ID:
        if allowed_chats_db.save(message.chat.id):
            await message.reply("Добавил чат!")
        else:
            await message.reply("Ошибка!")
@bot.on_message(filters.command(["del_chat"]))
async def add_admin_command(client: Client, message: Message):
    if message.from_user.id == OWNER_ID:
        if allowed_chats_db.delete(message.chat.id):
            await message.reply("Удалил чат!")
        else:
            await message.reply("Ошибка!")


@bot.on_message(filters.create(chat_check))
async def on_m(client: Client, message: Message):
    if db.find(message.text.lower()):
        await client.send_message(chat_id=message.chat.id,reply_to_message_id=message.id,text=db.find(message.text.lower()).info, disable_web_page_preview=True)
print("Ура, триггер бот запущен")
bot.run()