from typing import List

from fastapi import APIRouter, Request, status, Depends
from fastapi.responses import JSONResponse

from app.api_schemes import quest_schema
from app.services import quest_service


router = APIRouter(tags=['quest'])


# @router.get('/quest/{quest_id}', status_code=status.HTTP_200_OK, response_model=quest_schema)
# def get_quest(quest_id: int):
#     return quest_service.fetch_quest(quest_id)


@router.post('/quest', status_code=status.HTTP_201_CREATED)
def post_quest(data: quest_schema.CreateQuestModel):
    quest_service.create_quest(data)