import os
import platform
from datetime import datetime

def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    os.system(command)

def get_formatted_time():
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
