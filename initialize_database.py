"""
這個檔案負責創建 database schema, 其中包含以下資料表： 
users, workouts, exercises, sets, muscle groups
"""
import configparser
from sqlalchemy import create_engine
import pandas as pd
from models.base import Base
from models.user import User
from models.workout_set import WorkoutSet
from models.workout import Workout
from models.exercise import Exercise
from models.muscle_group import MuscleGroup

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

# 如果資料庫已存在則刪除
Base.metadata.drop_all(engine)

# 創建資料庫模型
Base.metadata.create_all(engine)

# 讀取 CSV 檔案
muscle_groups_df = pd.read_csv('data/muscle_groups.csv')
exercises_df = pd.read_csv('data/exercises.csv')
users_df = pd.read_csv('data/users.csv')
workouts_df = pd.read_csv('data/workouts.csv')
sets_df = pd.read_csv('data/sets.csv')

# 匯入數據到資料庫
muscle_groups_df.to_sql('muscle_groups', engine, index=False, if_exists='append')
exercises_df.to_sql('exercises', engine, index=False, if_exists='append')
users_df.to_sql('users', engine, index=False, if_exists='append')
workouts_df.to_sql('workouts', engine, index=False, if_exists='append')
sets_df.to_sql('sets', engine, index=False, if_exists='append')
