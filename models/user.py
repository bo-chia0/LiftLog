"""
這個檔案負責 users 資料表的定義
"""
from sqlalchemy import Column, Integer, String
from models.base import Base


class User(Base):
    """
    users 資料表儲存各使用者的資訊

    id: Primary Key
    email: 電子郵件
    password: 密碼
    username: 使用者名稱
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    username = Column(String(100), unique=True)
