from telegram import Bot
import asyncio

TOKEN = "8203096537:AAGkYY1IFmc6jloSfLL-kynA4x-qtZwzsC0"
CHAT_ID = 5612169007

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="📊 مرحباً! CryptoReport يعمل بنجاح! 🚀"
    )
    print("تم إرسال الرسالة!")

asyncio.run(main())
