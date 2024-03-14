import os
from dotenv import load_dotenv
load_dotenv()

config = {
  'token_bot': os.getenv('token_bot'),
}