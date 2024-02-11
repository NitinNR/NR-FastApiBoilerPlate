from dotenv import load_dotenv
load_dotenv()
import os

def getValue(key):
    return os.getenv(key)
