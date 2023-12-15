"""
這個檔案負責 exercises 資料表的定義
"""
from sqlalchemy import Column, Integer, String
from base import Base


class Exercise(Base):
    """
    exercises 資料表儲存各種運動的基本資訊
    """
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
