from models.session import Session
from models.muscle_group import MuscleGroup
from models.exercise import Exercise

def get_muscle_groups() -> list:
    """
    取得所有肌群

    回傳值：
    - list: 所有肌群
    """
    with Session() as session:
        muscle_groups = session.query(MuscleGroup).all()
        muscle_groups = [group.name for group in muscle_groups]
    
    return muscle_groups

def get_exercise_by_muscle_group(muscle_group: str) -> list:
    """
    取得指定肌群的所有動作

    參數：
    - muscle_group (str): 肌群名稱

    回傳值：
    - list: 所有動作
    """
    with Session() as session:
        muscle_group = session.query(MuscleGroup).filter(MuscleGroup.name == muscle_group).first()
        exercises = session.query(Exercise).filter(Exercise.muscle_group_id == muscle_group.id).all()
        exercises = [exercise.name for exercise in exercises]
    
    return exercises
