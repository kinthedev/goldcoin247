from pydantic import Field, HttpUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Dùng validation_alias để map chính xác tên biến môi trường (Ví dụ: BOT_TOKEN) vào biến code
    bot_token: SecretStr = Field(..., validation_alias="BOT_TOKEN")
    symbols_endpoint: HttpUrl = Field(..., validation_alias="SYMBOLS_ENDPOINT")

    # SỬA TẠI ĐÂY: Đồng bộ tên biến môi trường thực tế (PRICE_BASE_URL) với biến code của bạn
    price_base_url: HttpUrl = Field(..., validation_alias="PRICE_BASE_URL")

    # Cấu hình để đọc file .env
    model_config = SettingsConfigDict(
        env_file=".env",  # Đọc từ file .env nếu có
        env_file_encoding="utf-8",
        extra="ignore",  # Bỏ qua nếu trong môi trường/file .env có thừa biến khác, tránh lỗi extra_forbidden
    )


# Khởi tạo đối tượng settings
settings = Settings()
