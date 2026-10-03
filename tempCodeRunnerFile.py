import telebot

from bot.handlers import register_all_handlers
from config.settings import settings

bot = telebot.TeleBot(settings.bot_token.get_secret_value())

# Gọi trạm thu phát để nạp tất cả các lệnh vào bot
register_all_handlers(bot)

if __name__ == "__main__":
    print("🚀 Bot đang chạy...")
    bot.infinity_polling()
