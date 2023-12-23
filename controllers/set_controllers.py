from models.workout_set import WorkoutSet
from models.workout import Workout
from models.exercise import Exercise
from models.muscle_group import MuscleGroup
from models.user import User
from models.session import session

def add_set(workout_id: int, exercise_name: str, reps: int, weight: int):
    """
    新增一筆 set
    
    參數：
    - workout_id (int): 要新增的 workout ID。
    - exercise_name (str): 要新增的 exercise 名稱。
    - reps (int): 要新增的 reps 數量。
    - weight (int): 要新增的 weight 數量。
    """
    exercise = session.query(Exercise).filter(Exercise.name == exercise_name).first().id
    new_set = WorkoutSet(
        workout_id=workout_id,
        exercise_id=exercise,
        reps=reps,
        weight=weight
    )
    session.add(new_set)
    session.commit()

def get_set_records(workout_id: int, record_num: int) -> list:
    """
    獲取指定 workout ID 的最後 record_num 筆 sets
    
    參數：
    - workout_id (int): 要查詢的 workout ID。
    - record_num (int): 要返回的 set 數量。
    
    返回：
    - list: 一個 tuple 列表,每個 tuple 包含動作名稱、reps 和 weight。
    """
    set_record = (session.query(WorkoutSet, Exercise.name)
                  .join(Exercise, WorkoutSet.exercise_id == Exercise.id)
                  .filter(WorkoutSet.workout_id == workout_id)
                  .order_by(WorkoutSet.id.desc())
                  .limit(record_num)
                  .all()
                 )
    set_record = [
        (exercise_name, record.weight, record.reps) for record, exercise_name in set_record
    ]
    return set_record
