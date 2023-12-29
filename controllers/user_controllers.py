from models.user import User
from models.session import Session

def get_user_name_by_user_id(user_id: int) -> str:
    """
    取得指定 user ID 的 user name

    參數：
    - user_id (int): 要查詢的 user ID。

    返回：
    - str: user name
    """
    with Session() as session:
        user_name = (
            session.query(User)
            .filter_by(id=user_id)
            .first()
            .username
        )
        return user_name
    