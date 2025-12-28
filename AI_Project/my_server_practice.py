from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_Validator
import google.generativeai as genai
import config, logging, uvicorn

logging.basicConfig(
    filename = 'Dec28_server.log',
    levelname = logging.INFO,
    format = ('%(asctime)s - %(levelname)s - %(message)s')
)