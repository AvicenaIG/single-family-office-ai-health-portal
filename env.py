import os
from dotenv import load_dotenv, dotenv_values
import gradio as gr
print(gr.__version__)

load_dotenv(".env", override=False)  # take environment variables from ..env.
print(f"setting environment variables: {dotenv_values('.env')}")


def get_app_root():
    pass  # TODO: implement


def get_env_value(key):
    pass  # TODO: implement


if __name__ == '__main__':
