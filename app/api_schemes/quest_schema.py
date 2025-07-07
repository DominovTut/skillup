import typing
from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.constants.constants import QuestTypes, QuestStatus, QuestDifficulty


class BaseQuestModel(BaseModel):
    title: str
    quest_type: QuestTypes
    difficulty: QuestDifficulty

    model_config = ConfigDict(from_attributes=True)


class CreateQuestModel(BaseQuestModel):
    description: Optional[str]
    skill: str


class QuestInListModel(BaseQuestModel):
    id: int
    status: QuestStatus


class GetQuestModel(BaseQuestModel):
    description: Optional[str]
    skill_id: int
    status: QuestStatus
    xp_reward: int
