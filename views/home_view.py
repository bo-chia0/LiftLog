import flet as ft
from config import WIN_WIDTH, WIN_HEIGHT, CURRENT_USER_ID
from views.components import header_logo, create_bottom_app_bar, navigate_to_workout_page

def home_page(page: ft.Page):
    """
    Main Menu layout for the application.
    """
    # 視窗 properties
    page.title = "主頁"
    page.window_width = WIN_WIDTH
    page.window_height = WIN_HEIGHT

    """ 1st row: dropdown menus """
    exercise_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("option 1"),
            ft.dropdown.Option("option 2"),
            ft.dropdown.Option("option 3"),
        ],
        value="Option 1", width=WIN_WIDTH*0.3, height=WIN_HEIGHT*0.08
    )
    date_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("option 1"),
            ft.dropdown.Option("option 2"),
            ft.dropdown.Option("option 3"),
        ],
        value="Option 1", width=WIN_WIDTH*0.5, height=WIN_HEIGHT*0.08
    )
    dropdown_container = ft.Container(
        content=ft.Row(
            controls=[
                exercise_dropdown,
                date_dropdown
            ],
            alignment=ft.MainAxisAlignment.CENTER, spacing=10
        ),
        height=WIN_HEIGHT*0.1, bgcolor=ft.colors.RED
    )
    
    """ 2nd row: personal records """
    record_1 = ft.Text("60", size=30)
    record_2 = ft.Text("60", size=30)
    record_3 = ft.Text("60", size=30)
    record_container = ft.Container(
        content=ft.Row(
            controls=[
                record_1,
                record_2,
                record_3
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ), 
        height=WIN_HEIGHT*0.15, bgcolor=ft.colors.BLUE
    )
    
    """ 3rd row: Line charts """
    line_chart_container = ft.Container(
        height=WIN_HEIGHT*0.25, bgcolor=ft.colors.YELLOW)

    """ 4th row: Pie charts """
    pie_chart_container = ft.Container(
        height=WIN_HEIGHT*0.25, bgcolor=ft.colors.GREEN
    )

    """ navigation bar """
    page.bottom_appbar = create_bottom_app_bar()

    # Organize the layout using Rows and Columns
    page.add(
        ft.Column(
            controls=[
                header_logo,
                dropdown_container,
                record_container,
                line_chart_container,
                pie_chart_container
            ],
            alignment=ft.MainAxisAlignment.START, height=WIN_HEIGHT*0.9
        )
    )
    