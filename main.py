from fastapi import FastAPI
from fastapi.responses import JSONResponse
#from routes import summarise_route
from fastapi.middleware.cors import CORSMiddleware
from app import fetch_github_profile

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://github-api-content-fetcher.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/api/readme")
async def readme(repo: str):
    try:
        # not await fetch_github..as it is not a async fn 
        data =  fetch_github_profile(repo)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    

#app.include_router(summarise_route.router)
