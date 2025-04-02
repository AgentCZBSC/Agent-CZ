import openai
import os
from config import OPENAI_API_KEY

class AgentCZ:
    def __init__(self):
        self.api_key = OPENAI_API_KEY

    def chat(self, message: str) -> str:
        """
        Send a message to the AI and get a response.
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are Changpeng Zhao, the CEO of Binance."},
                      {"role": "user", "content": message}]
        )
        return response["choices"][0]["message"]["content"]
