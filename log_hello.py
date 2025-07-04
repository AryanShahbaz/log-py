from datetime import datetime
import pytz

# منطقه زمانی ایران
tehran = pytz.timezone("Asia/Tehran")

# گرفتن زمان فعلی
now = datetime.now(tehran).strftime("%Y-%m-%d %H:%M:%S")

# نوشتن در فایل
with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"{now} - Hello World\n")
