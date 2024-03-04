from dotenv import dotenv_values
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# Used to securely store your API key
from google.colab import userdata

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

env_data = dotenv_values('.env')
google_API = env_data['GOOGLE_API_KEY']
print(google_API)
