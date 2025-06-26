import typing
from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BaseSkillModel(BaseModel):
    title: str
    description: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class GetSkillModel(BaseSkillModel):
    id: int
    title: str
    description: Optional[str]
    current_lvl: int
    current_exp: int
    level_xp_cap: int


class CreateSkillModel(BaseSkillModel):
    pass


class SkillListModel(BaseModel):
    skills: List[GetSkillModel]