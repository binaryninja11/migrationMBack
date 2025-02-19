import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.views import router

app = FastAPI()


# ✅ Serve static files at both "/media" and "/test/media"
app.mount("/media", StaticFiles(directory="app/media"), name="media")
app.mount("/test/media", StaticFiles(directory="app/media"), name="test-media")  # Second mount

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",  # Common React dev server port
    "http://localhost:8000",
    "http://localhost:8001",
    "http://localhost:5177",  
    "http://10.10.3.71",  
    "http://localhost:80", 
    "https://migrationv-v1-0.onrender.com",  # server 
    "https://migrationagent.netlify.app",
    "https://migrationag.netlify.app",
    "https://migrationuz.netlify.app"
]
# http://10.10.3.71:8000
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Backend! (/docs for Swagger UI)"}

# if __name__ == '__main__':
#     uvicorn.run("main:app", reload=True)

if __name__ == '__main__':

    uvicorn.run("main:apppe", reload=True, host="0.0.0.0")
    # uvicorn.run("main:app", reload=True)

