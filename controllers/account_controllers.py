"""
這個檔案負責帳戶相關的功能，包括登入、註冊等
"""
from models.user import User
from models.session import Session


def register(email: str, password: str, username: str) -> None:
    """
    註冊新使用者

    參數：
    - email (str): 電子郵件
    - password (str): 密碼
    - username (str): 使用者名稱
    """
    with Session() as session:
        new_user = User(email=email, password=password, username=username)
        session.add(new_user)
        session.commit()


def login(email: str, password: str) -> User:
    """
    登入使用者

    參數：
    - email (str): 電子郵件
    - password (str): 密碼

    回傳值：
    - User: 使用者資訊
    """
    with Session() as session:
        user = session.query(User).filter_by(email=email, password=password).first()
    
    return user
