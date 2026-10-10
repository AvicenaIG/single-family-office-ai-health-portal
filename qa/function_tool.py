'''存放处理不同问答类型的工具函数，核心文件'''

import base64
from typing import Callable, List, Dict, Tuple
import time
import json
from client.clientfactory import Clientfactory
from qa.purpose_type import userPurposeType
from pathlib import Path
from ppt_docx.ppt_generation import generate as generate_ppt
from ppt_docx.ppt_content import generate_ppt_content
from ppt_docx.docx_generation import generate_docx_content as generate_docx
from ppt_docx.docx_content import generate_docx_content
from rag import rag_chain
from audio.audio_extract import (
)
from audio.audio_generate import audio_generate
from model.KG.search_service import search
from Internet.Internet_chain import InternetSearchChain
from Internet.youcom_search import research_news as youcom_research
from kg.Graph import GraphDao
from config.config import Config
from qa.purpose_type import userPurposeType
from env import get_env_value


_dao = GraphDao()

def is_file_path(path):
    pass  # TODO: implement

def relation_tool(entities: List[Dict] | None) -> str | None:
    pass  # TODO: implement









def check_entity(question: str) -> List[Dict]:
    pass  # TODO: implement


def KG_tool(
    pass  # TODO: implement
):




# 处理text问题的函数
def process_text_tool(
    pass  # TODO: implement
):


# 处理RAG问题
def RAG_tool(
    pass  # TODO: implement
):


# 处理ImageGeneration问题的函数
def process_images_tool(question_type, question, history, image_url=None):
    pass  # TODO: implement


def process_image_describe_tool(question_type, question, history, image_url=None):
    pass  # TODO: implement




def process_ppt_tool(
    pass  # TODO: implement
) -> Tuple[Tuple[str, str], userPurposeType]:


def process_docx_tool(
    pass  # TODO: implement
) -> Tuple[Tuple[str, str], userPurposeType]:


def process_text_video_tool(question_type, question, history, image_url=None):
    pass  # TODO: implement






# 处理audio问题的函数
def process_audio_tool(
    pass  # TODO: implement
):



# 处理联网搜索问题的函数
def process_InternetSearch_tool(
    pass  # TODO: implement
):


# 处理深度研究问题的函数
def YoucomResearch_tool(
    pass  # TODO: implement
):


QUESTION_TO_FUNCTION = {
}


# 根据用户不同的意图选择不同的函数
def map_question_to_function(purpose: userPurposeType) -> Callable:
    pass  # TODO: implement
