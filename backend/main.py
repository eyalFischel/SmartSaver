import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

"""
Description: 
This file is the main file for the backend. It will be used to run the backend API.
- Please try to keep this file as clean as possible.
- Only include the api routes, any other functions should be in a separate file.
- Please document the new apis you create on the repo's swagger documentation.
"""

app = FastAPI()

basefolder = os.path.dirname(__file__) 
load_dotenv(os.path.join(basefolder, ".env"))

# basic first route
@app.post('/example') 
async def root():
    try:
        return {"message": "Hello World!"}
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"Bad request. Invalid input data.")