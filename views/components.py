"""
儲存重複出現的 components
"""
import flet as ft
from config import WIN_WIDTH, WIN_HEIGHT

""" 頂部 header logo"""
header_logo = ft.Container(
    content=ft.Text(
        "LiftLog", size=35, weight=ft.FontWeight.W_900
    ),
    height=WIN_HEIGHT*0.1,
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
                    icon=ft.icons.PEOPLE
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        ),
        height=WIN_HEIGHT*0.1, bgcolor=ft.colors.GREY_500
    )

def navigate_to_home_page(e: ft.ControlEvent):
    from views.home_view import home_page
    e.page.controls.clear()
    home_page(e.page)

def navigate_to_workout_page(e: ft.ControlEvent):
    from views.workout_view import workout_page
    e.page.controls.clear()
    workout_page(e.page)
