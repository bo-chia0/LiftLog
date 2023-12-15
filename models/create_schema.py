"""
這個檔案負責創建 database schema, 其中包含以下資料表： 
users, workouts, exercises, sets, muscle groups
"""
import configparser
from sqlalchemy import create_engine
from base import Base
from user import User
from workout_set import WorkoutSet
from workout import Workout
from exercise import Exercise
from muscle_group import MajorMuscleGroup, MinorMuscleGroup, ExerciseMinorMuscleGroup

# 讀取配置檔案
config = configparser.ConfigParser()
config.read('config.ini')

# 從配置檔案中獲取資料庫信息
db_config = config['mysql']
username = db_config.get('user')
password = db_config.get('password')
host = db_config.get('host')
database = db_config.get('database')

# 創建資料庫連接
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')
# 以下宣告是為了避免 linter 警告
_ = [User, WorkoutSet, Workout, Exercise, \
     MajorMuscleGroup, MinorMuscleGroup, ExerciseMinorMuscleGroup]
# 創建資料庫模型
Base.metadata.create_all(engine)
