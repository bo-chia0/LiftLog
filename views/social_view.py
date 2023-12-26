import flet as ft
from config import GlobalConfig
from views.components import header_logo, create_bottom_app_bar
from controllers.workout_controllers import get_last_n_workout_ids, get_workout_info
from controllers.set_controllers import get_set_records

def social_page(page: ft.Page):
    """
    Social layout for the application.
    """
    # 視窗 properties
    page.title = "社交"
    page.window_width = GlobalConfig.WIN_WIDTH
    page.window_height = GlobalConfig.WIN_HEIGHT

    """ 所有用戶的訓練紀錄 """
    # 單一訓練紀錄
    def create_data_table(workout_id: int) -> list:
        set_records = get_set_records(workout_id, 5)
        set_rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(set_record[i])) for i in range(3)
                ]
            ) for set_record in set_records
        ]
        return set_rows
    def create_workout_record_by_id(workout_id: int) -> ft.Column:
        user_name, date_time = get_workout_info(workout_id)
        workout_record_info = ft.Row(
            controls=[
                ft.Text(f"{user_name}的訓練紀錄"),
                ft.Text(date_time)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        workout_record_data_table = ft.DataTable(
            columns=[
                    ft.DataColumn(ft.Text("動作")),
                    ft.DataColumn(ft.Text("重量"), numeric=True),
                    ft.DataColumn(ft.Text("次數"), numeric=True),
                ],
                rows=create_data_table(workout_id)
        )
        single_workout_record = ft.Container(
            ft.Column(
                controls=[
                    workout_record_info,
                    workout_record_data_table
                ],
            ),
            bgcolor=ft.colors.GREY_200
        )
        return single_workout_record

    # 全部訓練紀錄
    all_workout_records = ft.Container(
        ft.Column(
            controls=[
                create_workout_record_by_id(workout_id) for workout_id in get_last_n_workout_ids(10)
            ],
            scroll=ft.ScrollMode.ALWAYS, spacing=15
        ),
        height=GlobalConfig.WIN_HEIGHT*0.75
    )

    """ 統整 components """
    page.add(
        ft.Column(
            controls=[
                header_logo,
                all_workout_records
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )

    """ app bar """
    page.bottom_appbar = create_bottom_app_bar()
