"""
這個檔案負責 users 資料表的定義
"""
from sqlalchemy import Column, Integer, String
from models.base import Base


class User(Base):
    """
    users 資料表儲存各使用者的基本資訊
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    username = Column(String(100), unique=True)
