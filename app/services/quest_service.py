from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from app.database.db_connect import db_engine
from app.database.models import Quest
from app.api_schemes import quest_schema
from app.services import skills_service
from app.constants import constants


def calculate_xp_reward(difficulty: constants.QuestDifficulty, quest_type: constants.QuestTypes):
    match difficulty:
        case constants.QuestDifficulty.easy:
            diff = constants.EASY_QUEST_MULTIPLIER
        case constants.QuestDifficulty.medium:
            diff = constants.MEDIUM_QUEST_MULTIPLIER
        case constants.QuestDifficulty.hard:
            diff = constants.HARD_QUEST_MULTIPLIER

    match quest_type:
        case constants.QuestTypes.daily:
            q_type = constants.DAILY_BASE_QUEST_REWARD
        case constants.QuestTypes.weekly:
            q_type = constants.WEEKLY_BASE_QUEST_REWARD
        case constants.QuestTypes.monthly:
            q_type = constants.MONTHLY_BASE_QUEST_REWARD

    return q_type * diff



def create_quest(data: quest_schema.CreateQuestModel):
    with Session(db_engine) as session:
        # get associated skill and connect it to the data dict
        skill = skills_service.fetch_skill_by_title(data.skill)
        quest_dict = data.model_dump()
        quest_dict['skill'] = skill

        # calculate quest xp reward
        quest_dict['xp_reward'] = calculate_xp_reward(data.difficulty, data.quest_type)

        quest = Quest(**quest_dict)
        session.add(quest)
        session.commit()



def fetch_quest(quest_id: int):
    with Session(db_engine) as session:
        quest = session.query(Quest).where(Quest.id == quest_id).one()
        return quest


def fetch_all_quests():
    # with Session(db_engine) as session:
    #     skills = session.query(Skill).order_by(Skill.title).all()
    #     return skills_schema.SkillListModel(skills=[
    #         skills_schema.GetSkillModel.model_validate(skill) for skill in skills
    #     ])

    pass
