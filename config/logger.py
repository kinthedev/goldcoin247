import logging
import os

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/bot.log", encoding="utf-8"),  # Lưu ra file
        logging.StreamHandler(),  # Vẫn in ra màn hình terminal để bạn xem
    ],
)
logger = logging.getLogger("GoldCoinBot")
