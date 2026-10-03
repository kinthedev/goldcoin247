# import necessary lib
import requests
from cachetools import TTLCache, cached

from config.logger import logger
from config.settings import settings

price_base_url = settings.price_base_url
symbol_arrays = [
    {"name": "Silver", "symbol": "XAG"},
    {"name": "Gold", "symbol": "XAU"},
    {"name": "Bitcoin", "symbol": "BTC"},
    {"name": "Ethereum", "symbol": "ETH"},
    {"name": "Palladium", "symbol": "XPD"},
    {"name": "Copper", "symbol": "HG"},
    {"name": "Platinum", "symbol": "XPT"},
]

price_cache = TTLCache(maxsize=50, ttl=300)


# Dùng Decorator @cached để gắn bộ nhớ đệm này vào hàm
@cached(price_cache)
def get_price(symbol: str):
    # Check symbol is available
    logger.info(f"Đang gọi API lấy giá cho mã: {symbol}")
    symbol_is_valid = False
    for sy in symbol_arrays:
        if sy["symbol"] == symbol:
            symbol_is_valid = True
            break

    if not symbol_is_valid:
        return None

    try:
        url = f"{str(settings.price_base_url).rstrip('/')}/{symbol}/USD"
        response = requests.get(url, timeout=10)
        # Tự động chuyển xuống except nếu lỗi 404, 500,...
        response.raise_for_status()

        data = response.json()
        logger.info(f"Lấy giá {symbol} thành công!")
        # Lời khuyên: Bạn chỉ cần giá, nên bóc tách luôn ở đây
        # return data.get("price")
        return data  # Hoặc giữ nguyên trả cả cục data nếu bạn muốn
    except requests.exceptions.RequestException as e:
        # Bắt mọi loại lỗi mạng (timeout, 404, mất kết nối...)
        logger.error(f"Lỗi khi gọi API cho {symbol}. Chi tiết: {e}")
        return None
