import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

# 創建 Session 工廠，綁定到引擎
Session = sessionmaker(bind=engine)

# 創建一個 Session 實例
session = Session()
