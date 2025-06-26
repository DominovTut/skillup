from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Boolean, JSON, ARRAY
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

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

    