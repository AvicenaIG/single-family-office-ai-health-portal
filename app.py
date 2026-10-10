import base64
from qa.answer import get_answer
from qa.question_parser import parse_question
from qa.function_tool import process_image_describe_tool
from qa.purpose_type import userPurposeType
from audio.audio_generate import audio_generate

import PyPDF2
import chardet
import mimetypes
import gradio as gr
from icecream import ic
from docx import Document
from pydub import AudioSegment
import speech_recognition as sr
from opencc import OpenCC
import os


AVATAR = ("resource/user.png", "resource/bot.jpg")
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# pip install whisper
# pip install openai-whisper
# pip install soundfile
# pip install pydub
# pip install opencc-python-reimplemented


def convert_to_simplified(text):
    pass  # TODO: implement


def convert_audio_to_wav(audio_file_path):
    pass  # TODO: implement


def audio_to_text(audio_file_path):
    pass  # TODO: implement



# pip install PyPDF2
def pdf_to_str(pdf_file):
    pass  # TODO: implement


def docx_to_str(file_path):
    pass  # TODO: implement


# pip install chardet
def text_file_to_str(text_file):
    pass  # TODO: implement



def image_to_base64(image_path):
    pass  # TODO: implement


# 核心函数
def grodio_view(chatbot, chat_input):
    pass  # TODO: implement





















def gradio_audio_view(chatbot, audio_input):
    pass  # TODO: implement

















# 切换到语音模式的函数
def toggle_voice_mode():
    pass  # TODO: implement


# 切换回文本模式的函数
def toggle_text_mode():
    pass  # TODO: implement


examples = [
]


# 构建 Gradio 界面
with gr.Blocks() as demo:








# 启动应用
def start_gradio():
    pass  # TODO: implement


if __name__ == "__main__":
