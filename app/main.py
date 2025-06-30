from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.skills import router as skill_router
from app.api.quest import router as quest_router


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(skill_router)
app.include_router(quest_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)