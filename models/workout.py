"""
這個檔案負責 workouts 資料表的定義
"""
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Workout(Base):
    """
    workouts 資料表儲存每一次的訓練紀錄

    id: Primary Key
    user_id: 使用者 ID (ForeignKey)
    start_time: 開始時間
    end_time: 結束時間
    """
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    user = relationship("User")
