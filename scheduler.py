from telegram import Bot
import asyncio
import schedule
import time
import requests

TOKEN = "8203096537:AAGkYY1IFmc6jloSfLL-kynA4x-qtZwzsC0"
CHAT_ID = 5612169007

# محفظة المستخدم — الكميات وسعر الدخول فقط
portfolio = [
    {"symbol": "bitcoin", "name": "BTC", "quantity": 0.05, "entry_price": 42000},
    {"symbol": "ethereum", "name": "ETH", "quantity": 1.2, "entry_price": 2240},
    {"symbol": "solana", "name": "SOL", "quantity": 10, "entry_price": 98},
]

def get_prices():
    ids = ",".join([coin["symbol"] for coin in portfolio])
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)
    return response.json()

def generate_report():
    prices = get_prices()
    report = "📊 تقريرك اليومي — CryptoReport\n"
    report += "─────────────────────\n"
    total_pnl = 0
    for coin in portfolio:
        current_price = prices[coin["symbol"]]["usd"]
        pnl = (current_price - coin["entry_price"]) * coin["quantity"]
        pnl_percent = ((current_price - coin["entry_price"]) / coin["entry_price"]) * 100
        total_pnl += pnl
        emoji = "📈" if pnl > 0 else "📉"
        report += f"\n{emoji} {coin['name']}:\n"
        report += f"   الدخول: {coin['entry_price']}$ | الآن: {current_price:,.2f}$\n"
        report += f"   {'✅ ربح' if pnl > 0 else '⚠️ خسارة'}: {pnl:+.2f}$ ({pnl_percent:+.1f}%)\n"
    report += "\n─────────────────────\n"
    report += f"💼 إجمالي الربح/الخسارة: {total_pnl:+.2f}$\n"
    report += "─────────────────────\n"
    report += "⚠️ هذا التقرير للمعلومات فقط وليس نصيحة مالية."
    return report

def send_report():
    async def _send():
        bot = Bot(token=TOKEN)
        report = generate_report()
        await bot.send_message(chat_id=CHAT_ID, text=report)
        print("✅ تم إرسال التقرير!")
    asyncio.run(_send())

schedule.every().day.at("08:00").do(send_report)
print("⏰ Scheduler يعمل — التقرير سيصلك كل يوم الساعة 08:00")

send_report()

while True:
    schedule.run_pending()
    time.sleep(60)