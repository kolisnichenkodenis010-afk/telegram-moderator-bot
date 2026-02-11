import asyncio
import re
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

TOKEN = "8200665420:AAHea0o9zPYK75PKXsdIUDATnoqZaoB5Dqs"


JOB_KEYWORDS = [
    "работа", "вакансия", "вакансии",
    "подработка", "требуются", "зарплата",
    "удаленно", "удалённо"
]

LINK_RE = re.compile(r"(https?://|t\.me/|www\.)", re.IGNORECASE)

def contains_job(text):
    return any(word in text.lower() for word in JOB_KEYWORDS)

def contains_link(text):
    return bool(LINK_RE.search(text))

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    @dp.message(F.chat.type.in_({"group", "supergroup"}))
    async def moder(message: Message):
        text = (message.text or message.caption or "")

        if message.from_user and message.from_user.is_bot:
            await message.delete()
            return

        if text and contains_link(text):
            await message.delete()
            return

        if text and contains_job(text):
            await message.delete()
            return

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
