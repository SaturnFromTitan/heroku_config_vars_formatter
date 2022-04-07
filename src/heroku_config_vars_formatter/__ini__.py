"""
Note: This breaks if an environment variable is called `KEY`
"""
import pyperclip

from src.heroku_config_vars_formatter.formatting import format_text

text = pyperclip.paste()
res = format_text(text)
pyperclip.copy(res)