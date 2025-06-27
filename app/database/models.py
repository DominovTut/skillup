from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Boolean, Enum
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

from app.constants.constants import QuestTypes

Base = declarative_base()

class BaseEntity(Base):
    __abstract__ = True
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, onupdate=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())


class Skill(BaseEntity):
    __tablename__ = "Skill"
    title = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    current_lvl = Column(Integer, default=0)
    current_exp = Column(Integer, default=0)
    level_xp_cap = Column(Integer, default=100)
    quests = relationship("Quest", cascade="all, delete-orphan")


class Quest(BaseEntity):
    title = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    quest_type = Column(Enum(QuestTypes))
    status = Column(String(255)) # TODO make it Enum
    difficulty = Column(String(255)) # TODO make it Enum
    xp_reward = Column(Integer)
    skill = relationship("Skill", back_populates="quests", uselist=False)
    