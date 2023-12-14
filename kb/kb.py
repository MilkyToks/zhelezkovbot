from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb = InlineKeyboardMarkup(row_width=5)
ib1 = InlineKeyboardButton(text='Website',url='https://zhelezkov.net/')
ib2 = InlineKeyboardButton(text='Upwork',url='https://www.upwork.com/freelancers/sounddesign')
ib3 = InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/zhelezkov')
ib4 = InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/zhelezkov')
ib5 = InlineKeyboardButton(text='Write me', url='https://t.me/zhelezkov')
ikb.add(ib1, ib2).add(ib3, ib4).add(ib5)