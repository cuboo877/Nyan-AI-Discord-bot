from google import genai
import os
from dotenv import load_dotenv
from utils.config_loader import ConfigLoader
from utils.error_logger import ErrorLogger

load_dotenv()
#-------------

apiKey = os.getenv('gemini-apiKey')
client = genai.Client(api_key=apiKey)
model_name = ConfigLoader.get(key = "model")
role_prompt = ConfigLoader.get(key = "role")

async def request(prompt:str):
    prompt = role_prompt + prompt
    try:
        response = client.models.generate_content(
            model = model_name,
            contents = prompt
        )
        return response.text
    except Exception as e:
        print(e)
        ErrorLogger.log(error_msg = e) #先紀錄就好
        return f"嗚嗚嗚...人家不知道欸QQ"
