from aiogram.types import Message
from data import config
from boot import bot, dp, types
from kb.kb import ikb
from db.dbcon import db

@dp.message_handler(commands=['start'])
async def start_command(message):
    nonetype = ""
    user_id = message.from_user.id
    username = message.from_user.username or nonetype
    first_name = message.from_user.first_name
    db(user_id, username)
    await bot.send_message(chat_id=message.chat.id, text=f"""
Hello, <a href=\"tg://user?id={user_id}\">{first_name}</a>!
There's references to me 👇
"""
, reply_markup=ikb)