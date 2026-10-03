# Structure project

gold-coin-tracker-bot/
│
├── 📁 config/ # Cấu hình hệ thống
│ ├── **init**.py
│ └── settings.py # Đọc biến môi trường từ .env, thiết lập logging
│
├── 📁 src/ # Thư mục chứa mã nguồn chính
│ ├── **init**.py
│ │
│ ├── 📁 api/ # Lấy dữ liệu (API hoặc Crawl)
│ │ ├── **init**.py
│ │ ├── crypto_client.py # Gọi API Binance/CoinGecko
│ │ └── gold_crawler.py # Crawl hoặc gọi API giá vàng (SJC, PNJ...)
│ │
│ ├── 📁 bot/ # Logic điều khiển Bot
│ │ ├── **init**.py
│ │ ├── 📁 commands/ # Các lệnh (commands) của bot
│ │ │ ├── **init**.py
│ │ │ ├── start.py # Lệnh /start, /help
│ │ │ ├── gold.py # Lệnh /giavang
│ │ │ └── crypto.py # Lệnh /coin
│ │ └── handlers.py # Xử lý tin nhắn, sự kiện nút bấm (Callback)
│ │
│ ├── 📁 database/ # Lưu trữ dữ liệu (SQLite/PostgreSQL)
│ │ ├── **init**.py
│ │ ├── connection.py # Kết nối DB
│ │ └── models.py # Định nghĩa bảng (User, Alert) nếu dùng ORM (SQLAlchemy)
│ │
│ └── 📁 services/ # Logic xử lý, tính toán, định dạng
│ ├── **init**.py
│ └── formatter.py # Định dạng tin nhắn (thêm emoji 📈 📉, làm tròn số)
│
├── 📁 tests/ # Thư mục chứa file chạy thử nghiệm (pytest)
│
├── .env # Biến môi trường (BOT_TOKEN, DB_URL...)
├── .gitignore # Bỏ qua các file không cần thiết (venv, .env, **pycache**)
├── main.py # File chạy chính (Entry Point)
├── README.md # Hướng dẫn cài đặt và sử dụng dự án
└── requirements.txt # Danh sách các thư viện cần cài đặt (pip)
