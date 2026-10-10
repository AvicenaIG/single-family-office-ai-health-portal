'''大模型特征工程，让大模型输出json格式的数据'''
import json
import re
from typing import List, Dict
from client.clientfactory import Clientfactory

# 模拟一个用于生成 docx 内容的 JSON 模板
__output_format_docx = json.dumps({
}, ensure_ascii=True)

# 定义一个 prompt 用于生成 docx 内容
_GENERATE_DOCX_PROMPT_ = f'''请你根据用户要求生成docx的详细内容，不要省略。按这个JSON格式输出{__output_format_docx}，只能返回JSON，且JSON不要用```包裹，不要返回markdown格式'''

# 构造消息函数，历史记录被包括在内
def __construct_messages_docx(question: str, history: List[List | None]) -> List[Dict[str, str]]:
    pass  # TODO: implement



# 生成 docx 内容的函数
def generate_docx_content(question: str,
    pass  # TODO: implement



