#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
import T5

class Input_data(BaseModel):
    message: str

app = FastAPI()
model = "mamiksik/T5-commit-message-generation"

@app.post("/")
async def root(input_data: Input_data):
    print(input_data)
    llm=T5.T5(model)
    return {"message": f"{llm.do_quiet(input_data.message)}"}
    #return {"message": "Hello World."}

