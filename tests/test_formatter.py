import asyncio
import time


async def tai_file_async(ten_file):
    print(f"Bắt đầu tải {ten_file}...")
    await asyncio.sleep(2)  # Giả lập thời gian tải (Không làm "đứng" chương trình)
    print(f"✅ Đã tải xong {ten_file}!")


async def main_async():
    start_time = time.time()

    # Lệnh asyncio.gather giúp chạy tất cả tác vụ cùng một lúc
    await asyncio.gather(
        tai_file_async("File 1"), tai_file_async("File 2"), tai_file_async("File 3")
    )

    print(f"⏱️ Tổng thời gian (Bất đồng bộ): {time.time() - start_time:.2f} giây")


asyncio.run(main_async())
