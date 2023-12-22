"""
這個檔案負責 workouts 資料表的定義
"""
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Workout(Base):
    """
    workouts 資料表儲存每一次的訓練紀錄
    """
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    user = relationship("User")
