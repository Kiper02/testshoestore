from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardButton, WebAppInfo
from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command
import asyncio
import logging


logging.basicConfig(level=logging.INFO)

bot = Bot(token = "6699852067:AAFiE3yc_OeA8RQP4gJT7pGfIox0iqGdgT8")

dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Перейти", web_app=WebAppInfo(url='file:///C:/Users/%D0%9A%D0%B8%D1%80%D0%B8%D0%BB%D0%BB/Desktop/Python/%D0%91%D0%9E%D0%A2%D0%AB/ShoeShop/site.html')))
    
    await message.answer(
        "Выберите ссылку",
        reply_markup=builder.as_markup(),
    )




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())