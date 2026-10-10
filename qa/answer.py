'''根据问答类型选择对应的工具函数进行处理'''
from typing import Tuple, List, Any

from qa.function_tool import map_question_to_function

from qa.purpose_type import userPurposeType


def get_answer(
    pass  # TODO: implement
) -> Tuple[Any, userPurposeType]:

    function = map_question_to_function(question_type)
        pass  # TODO: implement


