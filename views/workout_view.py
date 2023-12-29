import flet as ft
from config import GlobalConfig
from views.components import header_logo, create_bottom_app_bar, dropdown_exercise, dropdown_muscle_group
from controllers.set_controllers import add_set, get_set_records
from controllers.workout_controllers import add_workout, end_current_workout

def workout_page(page: ft.Page):
    """
    紀錄目前訓練的頁面
    """
    # 視窗 properties
    page.title = "訓練"
    page.window_width = GlobalConfig.WIN_WIDTH
    page.window_height = GlobalConfig.WIN_HEIGHT

    """ 1st row: 新增一組訓練 """
    # 訓練動作
    text_muscle_group = ft.Text("部位")
    text_exercise = ft.Text("動作")
    row_exercise = ft.Row(
            controls=[
                text_muscle_group,
                dropdown_muscle_group,
                text_exercise,
                dropdown_exercise
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    #  訓練重量、次數
    text_weight = ft.Text("重量")
    textfield_weight = ft.TextField(
        width=GlobalConfig.WIN_WIDTH*0.35, height=GlobalConfig.WIN_HEIGHT*0.075
    )
    text_reps = ft.Text("次數")
    textfield_reps = ft.TextField(
        width=GlobalConfig.WIN_WIDTH*0.35, height=GlobalConfig.WIN_HEIGHT*0.075
    )
    # 統整重量、次數
    row_stats = ft.Row(
        controls=[
            text_weight,
            textfield_weight,
            text_reps,
            textfield_reps
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN    
    )

    #  新增按鈕
    def add_record(e: ft.ControlEvent):
        add_set(
            GlobalConfig.CURRENT_WORKOUT_ID,
            dropdown_exercise.value,
            int(textfield_reps.value),
            int(textfield_weight.value)
        )
        data_table.rows = update_data_table()
        page.update()

    button_add = ft.ElevatedButton(
        text="新增", on_click=add_record, width=GlobalConfig.WIN_WIDTH*0.35
    )
    row_button = ft.Row(controls=[button_add], alignment=ft.MainAxisAlignment.CENTER)

    # 統整新增一組訓練所需的元素
    new_record_container = ft.Container(
        content=ft.Column(
            controls=[
                row_exercise,
                row_stats,
                row_button
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        height=GlobalConfig.WIN_HEIGHT*0.22
    )

    """ 2nd row: 上次訓練的內容 """
    def update_data_table() -> list:
        set_records = get_set_records(GlobalConfig.CURRENT_WORKOUT_ID, 5)
        set_rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(set_record[i])) for i in range(3)
                ]
            ) for set_record in set_records
        ]
        return set_rows
    data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("動作")),
                ft.DataColumn(ft.Text("重量"), numeric=True),
                ft.DataColumn(ft.Text("次數"), numeric=True),
            ],
            rows=update_data_table()
    )
    data_table_container = ft.Container(
        content=data_table,
        height=GlobalConfig.WIN_HEIGHT*0.35
    )

    """ 3rd row: 開始或結束訓練按鈕 """
    def start_new_workout(e: ft.ControlEvent):
        if button_start.text == "開始新訓練":
            GlobalConfig.CURRENT_WORKOUT_ID = add_workout(GlobalConfig.CURRENT_USER_ID)
            data_table.rows = update_data_table()
            button_start.text = "結束訓練"
            page.update()
        else:
            end_current_workout(GlobalConfig.CURRENT_WORKOUT_ID)
            button_start.text = "開始新訓練"
            page.update()

    button_start = ft.ElevatedButton(
        text="開始新訓練",
        on_click=start_new_workout,
        width=GlobalConfig.WIN_WIDTH*0.35,  height=GlobalConfig.WIN_HEIGHT*0.075
    )
    button_container = ft.Container(
        content=ft.Row(
            controls=[button_start],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        height=GlobalConfig.WIN_HEIGHT*0.1
    )

    """ navigation bar """
    page.bottom_appbar = create_bottom_app_bar()

    """ 統整頁面所有元素 """
    page.add(
        ft.Column(
            controls=[
                header_logo,
                ft.Text("新增訓練", size=20),
                new_record_container,
                ft.Text("訓練紀錄", size=20),
                data_table_container,
                button_container
            ], 
            alignment=ft.MainAxisAlignment.START, spacing=3,
            height=GlobalConfig.WIN_HEIGHT*0.9
        )
    )
