from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse, RedirectResponse
from app.routers import emails
import uvicorn

app = FastAPI(title="Micro Sass EmailSender")

api = APIRouter(prefix="/api")
api.include_router(emails.router, tags=["Gmail"])

@app.get('/', tags=['Hello World'])
def main():
    return RedirectResponse(url='/docs')

app.include_router(api)

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000)