from env import get_env_value
from abc import abstractmethod

from openai import OpenAI
from openai import Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk

from typing import List, Dict


# 抽象类，用于构造client
class LLMclientbase(object):
    pass  # TODO: implement
    def __init__(self):
        pass  # TODO: implement

    def client(self):
        pass  # TODO: implement

    def model_name(self):
        pass  # TODO: implement

    def chat_with_ai(self, prompt: str) -> str | None:
        pass  # TODO: implement

    def chat_with_ai_stream(
        pass  # TODO: implement

    def construct_message(
        pass  # TODO: implement

    def chat_using_messages(self, messages: List[Dict]) -> str | None:
        pass  # TODO: implement
