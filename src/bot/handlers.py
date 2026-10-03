from src.bot.commands.crypto import register_crypto_command
from src.bot.commands.gold import register_gold_command
from src.bot.commands.start import register_start_command


def register_all_handlers(bot):
    register_start_command(bot)
    register_crypto_command(bot)
    register_gold_command(bot)
