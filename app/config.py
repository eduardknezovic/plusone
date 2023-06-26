
import os

"""
The code will first try to get the token from the OS environment variable TELEGRAM_TOKEN.
If there's no OS environment variable TELEGRAM_TOKEN, the code will use the hardcoded string.

For now, you can just replace the hardcoded string with your token and it will work fine.
"""

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', "Enter your telegram token here.")

