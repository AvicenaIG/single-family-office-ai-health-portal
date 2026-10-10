# retrieve类型有很多种,这个文件用于调用不同RAG类型接口
from rag.retrieve.retrieve_document import retrieve_docs
from typing import List
from openai import Stream
from openai.types.chat import ChatCompletionChunk
from client.clientfactory import Clientfactory



def invoke(question: str, history: List[List]) -> Stream[ChatCompletionChunk]:
    pass  # TODO: implement


