import os

from dotenv import load_dotenv
from fastapi import FastAPI
from app.routers.Transaction import router as transaction_router


"""
Description: 
This file is the main file for the backend. It will be used to run the backend API.
- Please try to keep this file as clean as possible.
- Only include the api routes, any other functions should be in a separate file.
- Please document the new apis you create on the repo's swagger documentation.
"""

app = FastAPI()
app.include_router(transaction_router)


basefolder = os.path.dirname(__file__)
load_dotenv(os.path.join(basefolder, ".env"))
