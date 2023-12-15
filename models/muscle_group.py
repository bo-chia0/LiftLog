"""
這個檔案負責 major_muscle_groups, minor_muscle_groups, exercise_minor_muscle_groups 資料表的定義
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class MajorMuscleGroup(Base):
    """
    major_muscle_groups 資料表儲存各主要肌群的基本資訊
    """
    __tablename__ = 'major_muscle_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

class MinorMuscleGroup(Base):
    """
    minor_muscle_groups 資料表儲存各次要肌群的基本資訊
    """
    __tablename__ = 'minor_muscle_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    major_group_id = Column(Integer, ForeignKey('major_muscle_groups.id'))
    major_group = relationship("MajorMuscleGroup")

class ExerciseMinorMuscleGroup(Base):
    """
    exercise_minor_muscle_group 資料表為 exercise 資料表與 minor_muscle_group 資料表之間的關聯
    """
    __tablename__ = 'exercise_minor_muscle_group'

    exercise_id = Column(Integer, ForeignKey('exercises.id'), primary_key=True)
    minor_muscle_group_id = Column(Integer, ForeignKey('minor_muscle_groups.id'), primary_key=True)
    exercise = relationship("Exercise")
    minor_muscle_group = relationship("MinorMuscleGroup")
    