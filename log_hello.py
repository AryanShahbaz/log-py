import time
from datetime import datetime
import pytz


tehran = pytz.timezone("Asia/Tehran")

while True:
    now = datetime.now(tehran).strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{now} - Hello World\n")
    # break
    time.sleep(60)
