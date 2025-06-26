from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from app.database.db_connect import db_engine
from app.database.models import Skill
from app.api_schemes import skills_schema


def create_skill(data: skills_schema.CreateSkillModel):
    with Session(db_engine) as session:
        skill = Skill(**data.model_dump())
        session.add(skill)
        session.commit()


def fetch_skill(skill_id: int):
    with Session(db_engine) as session:
        skill = session.query(Skill).where(Skill.id == skill_id).one()
        return skills_schema.GetSkillModel.model_validate(skill)


def fetch_all_skills():
    with Session(db_engine) as session:
        skills = session.query(Skill).order_by(Skill.title).all()
        return skills_schema.SkillListModel(skills=[
            skills_schema.GetSkillModel.model_validate(skill) for skill in skills
        ])
