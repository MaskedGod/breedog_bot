from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


img_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Get Photo", callback_data='photo')],
    [InlineKeyboardButton(text="Get Photos (5)", callback_data='photos')],
    ])