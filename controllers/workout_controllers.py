from datetime import datetime, timedelta
from sqlalchemy import func
from models.session import Session
from models.workout import Workout
from models.user import User
    
def add_workout(user_id: int) -> int:
    with Session() as session:
        new_workout = Workout(
            user_id=user_id,
            start_time=datetime.now()
        )
        session.add(new_workout)
        session.commit()
        return new_workout.id

def end_current_workout(workout_id: int) -> None:
    with Session() as session:
        workout = session.query(Workout).filter(Workout.id == workout_id).first()
        workout.end_time = datetime.now()
        session.commit()

def get_last_n_workout_ids(n: int) -> list:
    with Session() as session:
        workout_ids = [
            workout.id for workout in session
            .query(Workout)
            .order_by(Workout.id.desc())
            .limit(n)
        ]
    return workout_ids

def get_workout_info(workout_id: int) -> tuple():
    with Session() as session:
        workout = session.query(Workout).filter(Workout.id == workout_id).first()
        user_name = session.query(User).filter(User.id == workout.user_id).first().username
        date_time = workout.start_time.strftime("%Y-%m-%d %H:%M:%S")
    return user_name, date_time

def get_last_workout_id_by_user_id(user_id: int, n: int) -> int:
    with Session() as session:
        workout_ids = [workout.id for workout in (
            session.query(Workout)
            .filter(Workout.user_id == user_id)
            .order_by(Workout.id.desc())
            .limit(n)
        )]
    if len(workout_ids) > 0:
        return workout_ids
    else:
        return [None]

def get_recent_n_months_workout_count(user_id: int, months: int) -> list:
    """
    取得每一個月的訓練次數

    參數：
    - user_id (int): 要查詢的 user ID。
    - months (int): 要查詢的月份數量。

    返回：
    - list: 每個月的訓練次數。
    """
    # 計算查詢的起始日期
    start_date = datetime.now() - timedelta(days=30 * months)

    with Session() as session:
        # 構造查詢
        results = session.query(
            func.year(Workout.start_time).label('year'),
            func.month(Workout.start_time).label('month'),
            func.count().label('count')
        ).filter(
            Workout.user_id == user_id,
            Workout.start_time >= start_date
        ).group_by(
            'year', 'month'
        ).order_by(
            'year', 'month'
        ).all()

        # 將結果整理為列表
        workout_counts = [{'year': year, 'month': month, 'count': count} for year, month, count in results]
    
    return workout_counts

def get_recent_n_months_workout_time(user_id: int, months: int) -> list:
    """
    取得每一個月的訓練時間

    參數：
    - user_id (int): 要查詢的 user ID。
    - months (int): 要查詢的月份數量。

    返回：
    - list: 每個月的訓練時間。
    """
    # 計算查詢的起始日期
    start_date = datetime.now() - timedelta(days=30 * months)

    with Session() as session:
        # 構造查詢
        results = session.query(
            func.year(Workout.start_time).label('year'),
            func.month(Workout.start_time).label('month'),
            (func.sum(func.unix_timestamp(Workout.end_time) - func.unix_timestamp(Workout.start_time)) / 60.0).label('duration')
        ).filter(
            Workout.user_id == user_id,
            Workout.start_time >= start_date
        ).group_by(
            'year', 'month'
        ).order_by(
            'year', 'month'
        ).all()

        # 將結果整理為列表
        workout_times = [{'year': year, 'month': month, 'duration': duration} for year, month, duration in results]

    return workout_times