import os
from datetime import datetime

class ErrorLogger:
    filepath = 'logs/error.log'

    @classmethod
    def log(cls, error_msg: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{now}] {error_msg}\n"

        with open(cls.filepath, 'a', encoding='utf-8') as f:
            f.write(log_line)

        print(f"❌ Error logged: {log_line.strip()}")
