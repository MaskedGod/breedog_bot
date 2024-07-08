import asyncio
import os
import sys

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from private_chat_handler import private_chat_router

bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties())

dp = Dispatcher()
dp.include_router(private_chat_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    # await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())



asyncio.run(main())