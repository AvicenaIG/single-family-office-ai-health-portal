'''封装调用大模型代理的API接口的函数'''
from typing import List, Dict

from openai.types.chat import ChatCompletion, ChatCompletionChunk
from openai import Stream

from client.LLMclientbase import LLMclientbase
from overrides import override


# 实例化函数
class LLMclientgeneric(LLMclientbase):
    pass  # TODO: implement

    def __init__(self, *args, **krgs):
        pass  # TODO: implement

    def chat_with_ai(self, prompt: str) -> str | None:
        pass  # TODO: implement

    def chat_with_ai_stream(
        pass  # TODO: implement

    def construct_message(
        pass  # TODO: implement



    def chat_using_messages(self, messages: List[Dict]) -> str | None:
        pass  # TODO: implement

