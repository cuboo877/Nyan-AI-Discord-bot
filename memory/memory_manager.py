import json
import os
from typing import List, Dict
from datetime import datetime

class MemoryManager:
    def __init__(self, max_history: int = 5):
        self.max_history = max_history  # 最大保存的對話輪數
        self.history_file = "data/chat_history.json"
        self._ensure_history_file()

    def _ensure_history_file(self):
        """確保歷史記錄文件存在"""
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.history_file):
            with open(self.history_file, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def _load_history(self) -> Dict:
        """載入歷史記錄"""
        try:
            with open(self.history_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}

    def _save_history(self, history: Dict):
        """保存歷史記錄"""
        with open(self.history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

    def add_message(self, channel_id: str, author: str, content: str, is_bot: bool = False):
        """添加新的對話記錄"""
        history = self._load_history()
        
        if channel_id not in history:
            history[channel_id] = []

        # 添加新訊息
        message = {
            "author": author,
            "content": content,
            "is_bot": is_bot,
            "timestamp": datetime.now().isoformat()
        }
        
        history[channel_id].append(message)
        
        # 限制歷史記錄數量
        if len(history[channel_id]) > self.max_history:
            history[channel_id] = history[channel_id][-self.max_history:]
        
        self._save_history(history)

    def get_channel_history(self, channel_id: str) -> List[Dict]:
        """獲取指定頻道的歷史記錄"""
        history = self._load_history()
        return history.get(channel_id, [])

    def clear_channel_history(self, channel_id: str):
        """清除指定頻道的歷史記錄"""
        history = self._load_history()
        if channel_id in history:
            history[channel_id] = []
            self._save_history(history)

    def format_history_for_prompt(self, channel_id: str) -> str:
        """將歷史記錄格式化為 prompt 格式"""
        history = self.get_channel_history(channel_id)
        if not history:
            return ""

        formatted_history = []
        for msg in history:
            role = "助手" if msg["is_bot"] else "用戶"
            formatted_history.append(f"{role}: {msg['content']}")
        
        return "\n".join(formatted_history) 