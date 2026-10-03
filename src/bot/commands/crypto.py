# from src.api.crypto_client import get_price
import telebot

from config.settings import settings
from src.api.crypto_client import get_price

bot = telebot.TeleBot(settings.bot_token.get_secret_value())


# 2. Xử lý lệnh /coin
def register_crypto_command(bot):
    @bot.message_handler(commands=["coin"])
    def handle_coin_price(message):
        # message.text sẽ chứa toàn bộ tin nhắn, ví dụ: "/coin BTC"
        text = message.text.strip()

        # Cắt chuỗi theo khoảng trắng. Kết quả: ["/coin", "BTC"]
        parts = text.split()

        # Kiểm tra xem người dùng có gõ mã coin không (nghĩa là mảng phải có từ 2 phần tử trở lên)
        if len(parts) < 2:
            bot.reply_to(message, "⚠️️ Sếp quên nhập mã coin rồi! Ví dụ: /coin BTC")
            return  # Dừng hàm tại đây, không chạy xuống dưới nữa

        # Lấy phần tử thứ 2 (index 1) và chuyển thành chữ in hoa (phòng khi gõ /coin btc)
        symbol = parts[1].upper()

        # Báo cho người dùng biết bot đang xử lý (tránh cảm giác bot bị đơ)
        bot.reply_to(message, f"⏳ Đang lấy giá {symbol}...")

        # Gọi API
        data = get_price(symbol)

        # Xử lý kết quả trả về
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
