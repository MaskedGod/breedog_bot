from aiogram import F, Router
from aiogram.filters import CommandStart, Filter
from aiogram.types import Message, CallbackQuery

from dog_api import get_random_image, get_random_images
from keyboards import img_keyboard


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: Message) -> bool:
        return message.chat.type in self.chat_types
    

private_chat_router = Router()
private_chat_router.message.filter(ChatTypeFilter(["private"]))


@private_chat_router.message(CommandStart())
async def start_chat(message: Message):
    # await message.answer_photo(photo=get_random_image()[1],caption=f"Hello, this is {get_random_image()[0]}")
    await message.reply("Use /photo for one\n/photo_(1-10) to get any amount of photos\n or use a convenient menu ⬇️", reply_markup=img_keyboard)


@private_chat_router.message(F.text.startswith("/photo_"))
async def get_photos(message: Message):
    num = int(message.text.split("_")[1])
    photos = get_random_images(num)
    await message.answer_media_group([*photos])


@private_chat_router.message(F.text == "/photo")
async def get_photo(message: Message):
    cap, photo = get_random_image()
    await message.reply_photo(photo=photo, caption=cap, reply_markup=img_keyboard)


@private_chat_router.callback_query(F.data == "photo")
async def get_photo_callback(callback: CallbackQuery):
    cap, photo = get_random_image()
    await callback.answer("There it goes")
    await callback.message.reply_photo(photo=photo, caption=cap, reply_markup=img_keyboard)


@private_chat_router.callback_query(F.data == "photos")
async def get_photo_callback(callback: CallbackQuery):
    photos = get_random_images(5)
    await callback.answer("There it goes")
    await callback.message.reply_media_group(media=[*photos])
    await callback.message.reply("Choose an option:", reply_markup=img_keyboard)