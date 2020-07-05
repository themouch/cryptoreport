from telegram import Bot
import asyncio

TOKEN = "8203096537:AAGkYY1IFmc6jloSfLL-kynA4x-qtZwzsC0"
CHAT_ID = 5612169007

# بيانات وهمية للتطوير
portfolio = [
    {"symbol": "BTC", "quantity": 0.05, "entry_price": 42000, "current_price": 43850},
    {"symbol": "ETH", "quantity": 1.2, "entry_price": 2240, "current_price": 2198},
    {"symbol": "SOL", "quantity": 10, "entry_price": 98, "current_price": 103},
]

def generate_report(portfolio):
    report = "📊 تقريرك اليومي — CryptoReport\n"
    report += "─────────────────────\n"
    total_pnl = 0
    for coin in portfolio:
        pnl = (coin["current_price"] - coin["entry_price"]) * coin["quantity"]
        pnl_percent = ((coin["current_price"] - coin["entry_price"]) / coin["entry_price"]) * 100
        total_pnl += pnl
        emoji = "📈" if pnl > 0 else "📉"
        report += f"\n{emoji} {coin['symbol']}:\n"
        report += f"   الدخول: {coin['entry_price']}$ | الآن: {coin['current_price']}$\n"
        report += f"   {'✅ ربح' if pnl > 0 else '⚠️ خسارة'}: {pnl:+.2f}$ ({pnl_percent:+.1f}%)\n"
    report += "\n─────────────────────\n"
    report += f"💼 إجمالي الربح/الخسارة: {total_pnl:+.2f}$\n"
    report += "─────────────────────\n"
    report += "⚠️ هذا التقرير للمعلومات فقط وليس نصيحة مالية."
    return report

async def main():
    bot = Bot(token=TOKEN)
    report = generate_report(portfolio)
    await bot.send_message(chat_id=CHAT_ID, text=report)
    print("تم إرسال التقرير!")

asyncio.run(main())