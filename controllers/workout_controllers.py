from datetime import datetime
from models.session import session
from models.workout import Workout
    
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
