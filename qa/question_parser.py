'''问答类型判断函数，根据特定输入和大模型进行分类分类。'''
from typing import List, Dict

from client.clientfactory import Clientfactory

from qa.prompt_templates import get_question_parser_prompt
from qa.purpose_type import purpose_map
from qa.purpose_type import userPurposeType

from icecream import ic


def parse_question(question: str, image_url=None) -> userPurposeType:
    pass  # TODO: implement








