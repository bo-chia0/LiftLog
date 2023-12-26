"""
儲存重複出現的 components
"""
import flet as ft
from config import GlobalConfig
from controllers.muscle_group_controllers import get_muscle_groups, get_exercise_by_muscle_group

""" 頂部 header logo"""
header_logo = ft.Container(
    content=ft.Text(
        "LiftLog", size=35, weight=ft.FontWeight.W_900
    ),
    height=GlobalConfig.WIN_HEIGHT*0.1,
    alignment=ft.alignment.center,
    bgcolor=ft.colors.GREY_100,
)

""" navigation bar """
def create_bottom_app_bar():
    return ft.BottomAppBar(
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.HOME, on_click=navigate_to_home_page
                ),
                ft.IconButton(
                    icon=ft.icons.ADD, on_click=navigate_to_workout_page
                ),
                ft.IconButton(
                    icon=ft.icons.PEOPLE, on_click=navigate_to_social_page
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        ),
        height=GlobalConfig.WIN_HEIGHT*0.1, bgcolor=ft.colors.GREY_500
    )

def navigate_to_home_page(e: ft.ControlEvent):
    from views.home_view import home_page
    e.page.controls.clear()
    home_page(e.page)

def navigate_to_workout_page(e: ft.ControlEvent):
    from views.workout_view import workout_page
    e.page.controls.clear()
    workout_page(e.page)

def navigate_to_social_page(e: ft.ControlEvent):
    from views.social_view import social_page
    e.page.controls.clear()
    social_page(e.page)

""" 根據肌群選擇動作 """
# ------------------ 部位 ------------------ #
# 根據部位提供不同動作選項
def dropdown_muscle_group_change(e: ft.ControlEvent):
    update_dropdown_exercise(e)
    e.page.update()
# 製作下拉式選單
muscle_groups = get_muscle_groups()
dropdown_muscle_group = ft.Dropdown(
    options=[
        ft.dropdown.Option(group) for group in muscle_groups
    ], 
    value=muscle_groups[0], on_change=dropdown_muscle_group_change, 
    width=GlobalConfig.WIN_WIDTH*0.35, height=GlobalConfig.WIN_HEIGHT*0.075
)

# ------------------ 動作 ------------------ #
# 下拉式選單
dropdown_exercise = ft.Dropdown(
    width=GlobalConfig.WIN_WIDTH*0.35, height=GlobalConfig.WIN_HEIGHT*0.075
)
def update_dropdown_exercise(e: ft.ControlEvent):
    dropdown_exercise.options = [
        ft.dropdown.Option(exercise) for exercise in \
            get_exercise_by_muscle_group(dropdown_muscle_group.value)
    ]
    e.page.update()
