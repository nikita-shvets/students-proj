import uvicorn
from src.api import main_router
from fastapi import FastAPI
app = FastAPI()
app.include_router(main_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
