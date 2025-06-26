from typing import List

from fastapi import APIRouter, Request, status, Depends
from fastapi.responses import JSONResponse

from app.api_schemes import skills_schema
from app.services import skills_service


router = APIRouter(tags=['skills'])


@router.get('/skill', status_code=status.HTTP_200_OK, response_model=skills_schema.SkillListModel)
def get_all_memes():
    return skills_service.fetch_all_skills()


@router.get('/skill/{skill_id}', status_code=status.HTTP_200_OK, response_model=skills_schema.GetSkillModel)
def get_all_memes(skill_id: int):
    return skills_service.fetch_skill(skill_id)


@router.post('/skill', status_code=status.HTTP_201_CREATED)
def add_meme_to_favorite(data: skills_schema.CreateSkillModel):
    skills_service.create_skill(data)