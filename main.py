import time

import telebot

from config.logger import logger
from config.settings import settings
from src.bot.handlers import register_all_handlers

bot = telebot.TeleBot(settings.bot_token.get_secret_value())

# Gọi trạm thu phát để nạp tất cả các lệnh vào bot
register_all_handlers(bot)

if __name__ == "__main__":
    logger.info("Bot đang khởi động...")
    bot.infinity_polling()
    while True:
        try:
            logger.info("Đang kết nối với server Telegram...")
            bot.infinity_polling(timeout=60)
        except Exception as e:  # noqa
            logger.error(f"Bot bị lỗi :{e}")
            logger.info("Đang thử khởi động lại sau 5 giây")
            time.sleep(5)
