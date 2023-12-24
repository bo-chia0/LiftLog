import flet as ft
from config import WIN_WIDTH, WIN_HEIGHT, GlobalConfig
from views.components import header_logo, create_bottom_app_bar, dropdown_exercise, dropdown_muscle_group
from controllers.set_controllers import get_largest_weight, get_largest_weight_for_exercise

def home_page(page: ft.Page):
    """
    Main Menu layout for the application.
    """
    # 視窗 properties
    page.title = "主頁"
    page.window_width = WIN_WIDTH
    page.window_height = WIN_HEIGHT
    
    """ 2nd row: personal records """
    # ------------------ 個人紀錄 ------------------ #
    text_personal_record = ft.Text("個人紀錄", size=30)
    text_personal_record_weight = ft.Text(size=50)
    personal_record = ft.Column(
        controls=[
            text_personal_record,
            text_personal_record_weight
        ],
        spacing=0
    )
    # ------------------ 排名紀錄 ------------------ #
    text_rank_record = ft.Text("排名紀錄", size=30)
    text_rank_record_weight = ft.Text(size=50)
    text_rank_record_holder = ft.Text()
    rank_record = ft.Column(
        controls=[
            text_rank_record,
            ft.Row(
                controls=[
                    text_rank_record_weight,
                    text_rank_record_holder
                ]
            )
        ],
        spacing=0
    )

    def update_records(e: ft.ControlEvent):
        text_personal_record_weight.value = (
            get_largest_weight(GlobalConfig.CURRENT_USER_ID, dropdown_exercise.value)
        )
        all_record, all_record_holder = get_largest_weight_for_exercise(dropdown_exercise.value)
        text_rank_record_weight.value = all_record
        text_rank_record_holder.value = "by " + all_record_holder
        e.page.update()

    record_container = ft.Container(
        content=ft.Row(
            controls=[
                personal_record,
                rank_record
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        ), 
        height=WIN_HEIGHT*0.15, bgcolor=ft.colors.BLUE
    )

    """ 1st row: dropdown menus """
    dropdown_exercise.on_change = update_records
    dropdown_container = ft.Container(
        content=ft.Row(
            controls=[
                dropdown_muscle_group,
                dropdown_exercise
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        ),
        height=WIN_HEIGHT*0.1, bgcolor=ft.colors.RED
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
            alignment=ft.MainAxisAlignment.START, height=WIN_HEIGHT*0.9, spacing=0
        )
    )
    