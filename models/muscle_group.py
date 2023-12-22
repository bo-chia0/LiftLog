"""
這個檔案負責 major_muscle_groups, minor_muscle_groups, exercise_minor_muscle_groups 資料表的定義
"""
from sqlalchemy import Column, Integer, String
from models.base import Base


class MuscleGroup(Base):
    """
    muscle_groups 資料表儲存各主要肌群的基本資訊
    """
    __tablename__ = 'muscle_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    