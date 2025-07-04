from datetime import datetime

with open("log.txt", "a", encoding="utf-8") as f:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{now} - Hello World\n")
