from datetime import datetime
from models.session import session
from models.workout import Workout
from models.user import User
    
def add_workout(user_id: int) -> int:
    new_workout = Workout(
        user_id=user_id,
        start_time=datetime.now()
    )
    session.add(new_workout)
    session.commit()
    return new_workout.id

def end_current_workout(workout_id: int) -> None:
    workout = session.query(Workout).filter(Workout.id == workout_id).first()
    workout.end_time = datetime.now()
    session.commit()

def get_last_n_workout_ids(n: int) -> list:
    return [
        workout.id for workout in session
        .query(Workout)
        .order_by(Workout.id.desc())
        .limit(n)
    ]

def get_workout_info(workout_id: int) -> tuple():
    workout = session.query(Workout).filter(Workout.id == workout_id).first()
    user_name = session.query(User).filter(User.id == workout.user_id).first().username
    date_time = workout.start_time.strftime("%Y-%m-%d %H:%M:%S")
    return user_name, date_time

def get_last_workout_id_by_user_id(user_id: int, n: int) -> int:
    return [workout.id for workout in (
        session.query(Workout)
        .filter(Workout.user_id == user_id)
        .order_by(Workout.id.desc())
        .limit(n)
    )]

