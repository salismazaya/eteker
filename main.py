# load .env
from dotenv import load_dotenv
from pathlib import Path

env_path_file = Path(__file__).parent / '.env'
load_dotenv(env_path_file)
# end load .env

from fastapi import FastAPI

app = FastAPI()
