import openai
import os
from dotenv import load_dotenv
from chatbot import AgentCZ

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    agent = AgentCZ()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = agent.chat(user_input)
        print("CZ:", response)
