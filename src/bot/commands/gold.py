import telebot

from config.settings import settings
from src.api.crypto_client import get_price

bot = telebot.TeleBot(settings.bot_token.get_secret_value())


def register_gold_command(bot):
    @bot.message_handler(commands=["giavang"])
    def handle_gold_price(message, symbol="XAU"):
        data = get_price(symbol)
        if data is None:
            bot.reply_to(
                message, f"❌ Không tìm thấy giá cho mã {symbol} hoặc API đang lỗi."
            )
        else:
            # Lấy con số giá trị (giả sử JSON trả về có key 'price')
            price = data.get("price")
            # Format giá trị hiển thị đẹp hơn
            bot.reply_to(
                message,
                f"💰 Giá {symbol} hiện tại là: **${price:,.2f}**",
                parse_mode="Markdown",
            )
