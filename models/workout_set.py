"""
這個檔案負責 sets 資料表的定義
"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class WorkoutSet(Base):
    """
    sets 資料表儲存訓練組的資訊

    id: Primary Key
    workout_id: 當次訓練 ID (ForeignKey)
    exercise_id: 訓練動作 ID (ForeignKey)
    reps: 次數
    weight: 重量
    """
    __tablename__ = 'sets'

    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    reps = Column(Integer)
    weight = Column(Integer)
    workout = relationship("Workout")
    exercise = relationship("Exercise")
