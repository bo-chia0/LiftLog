"""
這個檔案負責 sets 資料表的定義
"""
from sqlalchemy import Column, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class WorkoutSet(Base):
    """
    sets 資料表儲存訓練組的資訊（重量、次數等）
    """
    __tablename__ = 'sets'

    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    reps = Column(Integer)
    weight = Column(DECIMAL)
    workout = relationship("Workout")
    exercise = relationship("Exercise")
