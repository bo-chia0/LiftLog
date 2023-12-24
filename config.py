"""
定義 views 共用的參數
"""
WIN_WIDTH = 400
WIN_HEIGHT = 800

"""
目前使用的 User 和 Workout ID
"""
class GlobalConfig:
    CURRENT_USER_ID = None
    CURRENT_WORKOUT_ID = None

    @classmethod
    def set_current_user_id(cls, user_id):
        cls.CURRENT_USER_ID = user_id

    @classmethod
    def set_current_workout_id(cls, workout_id):
        cls.CURRENT_WORKOUT_ID = workout_id
