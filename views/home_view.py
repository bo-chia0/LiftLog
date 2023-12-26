import flet as ft
from config import WIN_WIDTH, WIN_HEIGHT, GlobalConfig
from views.components import header_logo, create_bottom_app_bar, dropdown_exercise, dropdown_muscle_group
from controllers.set_controllers import get_largest_weight, get_largest_weight_for_exercise, get_exercise_max_weight_each_workout, get_muscle_groups_portion
from controllers.workout_controllers import get_recent_n_months_workout_count
from controllers.muscle_group_controllers import get_muscle_groups

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
        # 更新個人紀錄
        text_personal_record_weight.value = (
            get_largest_weight(GlobalConfig.CURRENT_USER_ID, dropdown_exercise.value)
        )
        all_record, all_record_holder = get_largest_weight_for_exercise(dropdown_exercise.value)
        text_rank_record_weight.value = all_record
        text_rank_record_holder.value = "by " + all_record_holder
        # 更新折線圖
        line_chart_data = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(i, value) for i, (workout_id, value) \
                        in enumerate(sorted(
                            get_exercise_max_weight_each_workout(
                                GlobalConfig.CURRENT_USER_ID, dropdown_exercise.value
                            ).items()
                        )
                    )
                ],
                stroke_width=3,
                color=ft.colors.LIGHT_GREEN,
                curved=True
            )
        ]
        line_chart_container.content = ft.LineChart(
            data_series=line_chart_data,
            horizontal_grid_lines=ft.ChartGridLines(
                interval=5, width=0.5,
                color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)
            ),
            vertical_grid_lines=ft.ChartGridLines(
                interval=1, width=0.5,
                color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)
            ),
            left_axis=ft.ChartAxis(
                labels_size=0,
                title=ft.Text("重量 (kg)"),
                title_size=30
            ),
            bottom_axis=ft.ChartAxis(
                labels_size=0,
                title=ft.Text("訓練 (次)"),
                title_size=30
            ),
            border=ft.border.all(1, ft.colors.GREY_400)
        )
        e.page.update()

    record_container = ft.Container(
        content=ft.Row(
            controls=[
                personal_record,
                rank_record
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        ), 
        height=WIN_HEIGHT*0.15
    )
    
    """ 3rd row: Line charts """
    line_chart_container = ft.Container(
        height=WIN_HEIGHT*0.25
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
        height=WIN_HEIGHT*0.1
    )

    """ 4th row: Bar charts """
    workout_count_chart = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x=i,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=result['count'],
                        width=20,                        
                        color=ft.colors.BLACK54,
                        tooltip=str(result['count']),
                        border_radius=0,
                    ),
                ],
            ) for i, result in enumerate(get_recent_n_months_workout_count(GlobalConfig.CURRENT_USER_ID, 6))
        ],
        border=ft.border.all(1, ft.colors.GREY_400),
        left_axis=ft.ChartAxis(
            labels_size=0,
            title=ft.Text("訓練次數"), title_size=25
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=i, label=ft.Container(
                        ft.Text(f"{result['month']:02d}-{result['year']%100}"), 
                        padding=10
                    )
                ) for i, result in enumerate(get_recent_n_months_workout_count(GlobalConfig.CURRENT_USER_ID, 6))
            ], labels_size=40,
            title=ft.Text("月－年"), title_size=20
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, interval=5, width=1
        )
    )
    bar_chart_container = ft.Container(
        content=workout_count_chart,
        height=WIN_HEIGHT*0.3
    )

    """ 5th row: Pie charts """
    muscle_groups = get_muscle_groups()
    color = [
        ft.colors.AMBER, ft.colors.BLUE, ft.colors.GREEN, ft.colors.LIME, ft.colors.ORANGE, ft.colors.PINK
    ]
    muscle_group_proportion_pie_chart = ft.PieChart(
        sections=[
            ft.PieChartSection(
                100*get_muscle_groups_portion(i+1, GlobalConfig.CURRENT_USER_ID),
                title=f"{muscle_groups[i]}\n{100*get_muscle_groups_portion(i+1, GlobalConfig.CURRENT_USER_ID):.2f}%",
                color=color[i]
            ) for i in range(6)
        ]
    )
    pie_chart_container = ft.Container(
        content=muscle_group_proportion_pie_chart,
        height=WIN_HEIGHT*0.25
    )

    """ 6th row: Data Table """
    data_table_container = ft.Container(
        height=WIN_HEIGHT*0.25, bgcolor=ft.colors.BLUE
    )

    """ Organize the layout using Columns """
    statistics = ft.Container(
        ft.Column(
                controls=[
                    dropdown_container,
                    record_container,
                    line_chart_container,
                    bar_chart_container,
                    pie_chart_container,
                    data_table_container
                ],
                scroll=ft.ScrollMode.ALWAYS
        ),
        height=WIN_HEIGHT*0.75
    )       

    """ navigation bar """
    page.bottom_appbar = create_bottom_app_bar()

    # Organize the layout using Rows and Columns
    page.add(
        ft.Column(
            controls=[
                header_logo,
                statistics
            ],
            alignment=ft.MainAxisAlignment.START, height=WIN_HEIGHT*0.9, spacing=0
        )
    )
    