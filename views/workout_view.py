import flet as ft
from config import WIN_WIDTH, WIN_HEIGHT, GlobalConfig
from views.components import header_logo, create_bottom_app_bar
from controllers.set_controllers import add_set, get_set_records
from controllers.muscle_group_controllers import get_muscle_groups, get_exercise_by_muscle_group
from controllers.workout_controllers import add_workout, end_current_workout

def workout_page(page: ft.Page):
    """
    Workout layout for the application.
    """
    # 視窗 properties
    page.title = "訓練"
    page.window_width = WIN_WIDTH
    page.window_height = WIN_HEIGHT

    """ 1st row: new record """
    # ------------------ 部位 ------------------ #
    text_muscle_group = ft.Text("部位")
    # 根據部位提供不同動作選項
    def dropdown_muscle_group_change(e: ft.ControlEvent):
        exercises = get_exercise_by_muscle_group(dropdown_muscle_group.value)
        dropdown_exercise.options = [
            ft.dropdown.Option(exercise) for exercise in exercises
        ]
        page.update()
    # 製作下拉式選單
    muscle_groups = get_muscle_groups()
    dropdown_muscle_group = ft.Dropdown(
        options=[
            ft.dropdown.Option(group) for group in muscle_groups
        ], 
        value=muscle_groups[0], on_change=dropdown_muscle_group_change, 
        width=WIN_WIDTH*0.35, height=WIN_HEIGHT*0.075
    )

    # ------------------ 動作 ------------------ #
    text_exercise = ft.Text("動作")
    # 下拉式選單
    exercises = get_exercise_by_muscle_group(dropdown_muscle_group.value)
    dropdown_exercise = ft.Dropdown(
        options=[
            ft.dropdown.Option(exercise) for exercise in exercises
        ],
        width=WIN_WIDTH*0.35, height=WIN_HEIGHT*0.075
    )
    row_exercise = ft.Row(
            controls=[
                text_muscle_group,
                dropdown_muscle_group,
                text_exercise,
                dropdown_exercise
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    
    # ------------------ 訓練資訊 ------------------ #
    text_weight = ft.Text("重量")
    textfield_weight = ft.TextField(
        width=WIN_WIDTH*0.35, height=WIN_HEIGHT*0.075
    )
    text_reps = ft.Text("次數")
    textfield_reps = ft.TextField(
        width=WIN_WIDTH*0.35, height=WIN_HEIGHT*0.075
    )

    row_stats = ft.Row(
        controls=[
            text_weight,
            textfield_weight,
            text_reps,
            textfield_reps
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN    
    )

    # ------------------ 新增按鈕 ------------------ #
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
        text="新增", on_click=add_record, width=WIN_WIDTH*0.35
    )
    row_button = ft.Row(controls=[button_add], alignment=ft.MainAxisAlignment.CENTER)

    # ------------------ 合併 ------------------ #
    new_record_container = ft.Container(
        content=ft.Column(
            controls=[
                row_exercise,
                row_stats,
                row_button
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        height=WIN_HEIGHT*0.22#, bgcolor=ft.colors.RED
    )

    """ 2nd row: data table """
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
        height=WIN_HEIGHT*0.4#, bgcolor=ft.colors.BLUE
    )

    """ 3rd row: start/end exercise button """
    def start_new_workout(e: ft.ControlEvent):
        if button_start.text == "開始訓練":
            GlobalConfig.CURRENT_WORKOUT_ID = add_workout(GlobalConfig.CURRENT_USER_ID)
            data_table.rows = update_data_table()
            button_start.text = "結束訓練"
            page.update()
        else:
            end_current_workout(GlobalConfig.CURRENT_WORKOUT_ID)
            button_start.text = "開始訓練"
            page.update()

    button_start = ft.ElevatedButton(
        text="開始訓練",
        on_click=start_new_workout,
        width=WIN_WIDTH*0.35,  height=WIN_HEIGHT*0.075
    )
    button_container = ft.Container(
        content=ft.Row(
            controls=[button_start],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        height=WIN_HEIGHT*0.1#, bgcolor=ft.colors.GREEN
    )

    """ navigation bar """
    page.bottom_appbar = create_bottom_app_bar()

    # 用戶信息和目標
    page.add(
        ft.Column(
            controls=[
                header_logo,
                new_record_container,
                data_table_container,
                button_container
            ], 
            alignment=ft.MainAxisAlignment.START,
            height=WIN_HEIGHT*0.9
        )
    )

