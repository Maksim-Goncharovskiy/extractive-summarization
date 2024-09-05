from fastapi import FastAPI
from src.handlers import router as extract_router
import os
import uvicorn

app = FastAPI(title="Extract Summarizer")

app.include_router(extract_router)

if __name__ == '__main__':
    HOST = str(os.getenv("HOST"))
    PORT = int(os.getenv("PORT"))
    
    uvicorn.run(app, host=HOST, port=PORT)
