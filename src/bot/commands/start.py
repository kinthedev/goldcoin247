# from src.api.crypto_client import get_price
import telebot

from config.settings import settings

bot = telebot.TeleBot(settings.bot_token.get_secret_value())


def register_start_command(bot):
    @bot.message_handler(commands=["start", "help"])
    def send_welcome(message):
        bot.reply_to(message, "Chào sếp! Gõ /coin BTC để xem giá bitcoin nhé.")
