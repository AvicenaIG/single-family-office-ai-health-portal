'''向外部构建不同大模型代理的接口，构建完成后返回一个大模型代理'''
from client.ourAPI.client import OurAPI
from client.zhipuAPI.client import Image_generate_client, Image_describe_client
from client.zhipuAPI.client import Video_generate_client
from env import get_env_value
from qa.purpose_type import userPurposeType


class Clientfactory:
    pass  # TODO: implement

    def __init__(self):
        pass  # TODO: implement

    def get_client(self):
        pass  # TODO: implement

    def get_special_client(client_type: str):
        pass  # TODO: implement

