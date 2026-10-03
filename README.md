# Gold & Crypto Tracker Bot 🤖

Telegram Bot theo dõi và tra cứu giá vàng (SJC, PNJ...) và tiền điện tử (Binance, CoinGecko).

## 📁 Cấu trúc dự án

```structure
gold-coin-tracker-bot/
├── config/             # Cấu hình hệ thống & biến môi trường
├── src/                # Mã nguồn chính
│   ├── api/            # API client (Crypto) và Crawler (Giá vàng)
│   ├── bot/            # Logic điều khiển Telegram Bot & commands
│   ├── database/       # Kết nối cơ sở dữ liệu & models
│   └── services/       # Xử lý logic, định dạng dữ liệu & thông báo
├── tests/              # Test cases (pytest)
├── .env                # Biến môi trường
├── main.py             # Entrypoint khởi chạy ứng dụng
└── requirements.txt    # Danh sách thư viện phụ thuộc
```

## 🚀 Cài đặt & Khởi chạy

Bot Telegram thông báo giá Vàng và Crypto theo thời gian thực, hỗ trợ Caching chống nghẽn API và tự động ghi Log hệ thống.

## Hướng dẫn cài đặt

**1. Clone dự án về máy**
`bash
git clone https://github.com/Tên_Của_Bạn/Goldcoin247.git
cd Goldcoin247
`
**2. Tạo và kích hoạt môi trường ảo (Virtual Environment)**

## Trên Linux/macOS

`bash
python -m venv .venv
source .venv/bin/activate
`

## Trên Windows

`bash
python -m venv .venv
.venv\Scripts\activate
`

**3. Cài đặt các thư viện cần thiết**
`bash
pip install -r requirements.txt
`
**4. Cấu hình Bot**

## bot

* Copy file `.env.example` và đổi tên thành `.env`.
* Mở file `.env` và điền `BOT_TOKEN` lấy từ @BotFather trên Telegram.

**5. Khởi chạy**
`bash
python main.py
`
# goldcoin247
