from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from app.database.db_connect import db_engine
from app.database.models import Quest
from app.api_schemes import quest_schema
from app.services import skills_service


def create_quest(data: quest_schema.CreateQuestModel):
    # with Session(db_engine) as session:
    #     skill = Skill(**data.model_dump())
    #     session.add(skill)
    #     session.commit()

    with Session(db_engine) as session:
        skill = skills_service.fetch_skill_by_title(data.skill)
        quest_dict = data.model_dump()
        quest_dict['skill'] = skill
        quest = Quest(**quest_dict)
        session.add(quest)
        session.commit()



def fetch_quest(quest_id: int):
    # with Session(db_engine) as session:
    #     skill = session.query(Skill).where(Skill.id == skill_id).one()
    #     return skills_schema.GetSkillModel.model_validate(skill)

    pass


def fetch_all_quests():
    # with Session(db_engine) as session:
    #     skills = session.query(Skill).order_by(Skill.title).all()
    #     return skills_schema.SkillListModel(skills=[
    #         skills_schema.GetSkillModel.model_validate(skill) for skill in skills
    #     ])

    pass
