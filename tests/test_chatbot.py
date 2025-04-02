import unittest
from src.chatbot import AgentCZ

class TestAgentCZ(unittest.TestCase):
    def setUp(self):
        self.agent = AgentCZ()

    def test_chat_response(self):
        response = self.agent.chat("What is Binance?")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

if __name__ == "__main__":
    unittest.main()
