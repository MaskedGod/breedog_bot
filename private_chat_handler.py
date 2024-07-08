import re
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Filter
from aiogram.types import Message, CallbackQuery

from dog_api import get_random_image, get_random_images


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types
    

private_chat_router = Router()
private_chat_router.message.filter(ChatTypeFilter(["private"]))


@private_chat_router.message(CommandStart())
async def start_chat(message: types.Message):
    # await message.answer_photo(photo=get_random_image()[1],caption=f"Hello, this is {get_random_image()[0]}")
    await message.reply("Use /photo for one\n/photo_(1-10) to get any amount of photos", reply_markup=photos_keyboard)


@private_chat_router.message(F.text.startswith("/photo_"))
async def get_photo(message: types.Message):
    num = int(message.text.split("_")[1])
    photos = get_random_images(num)
    await message.answer_media_group([*photos])


@private_chat_router.message(F.text == "/photo")
async def get_photo(message: types.Message):
    cap, photo = get_random_image()
    await message.answer_photo(photo=photo,caption=cap)