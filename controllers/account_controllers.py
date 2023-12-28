"""
這個檔案負責帳戶相關的功能，包括登入、註冊、忘記密碼等
"""
from models.user import User
from models.session import Session


def register(email, password, username):
    """
    註冊新使用者
    """
    with Session() as session:
        new_user = User(email=email, password=password, username=username)
        session.add(new_user)
        session.commit()


def login(email, password):
    """
    登入使用者
    """
    with Session() as session:
        user = session.query(User).filter_by(email=email, password=password).first()
    
    return user
