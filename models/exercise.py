"""
這個檔案負責 exercises 資料表的定義
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Exercise(Base):
    """
    exercises 資料表儲存各種運動的基本資訊
    """
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    muscle_group_id = Column(Integer, ForeignKey('muscle_groups.id'))
    muscle_group = relationship("MuscleGroup")
