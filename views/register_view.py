import flet as ft
from flet import Row, Column
from controllers.account_controllers import register
from config import GlobalConfig


def register_page(page: ft.Page):
    # window properties
    page.title = "Register"
    page.window_width = GlobalConfig.WIN_WIDTH
    page.window_height = GlobalConfig.WIN_HEIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # elements
    text_email: ft.TextField = ft.TextField(
        label="電子郵件", width=250, height=50
        )
    text_username: ft.TextField = ft.TextField(
        label="使用者名稱", width=250, height=50
        )
    text_password: ft.TextField = ft.TextField(
        label="密碼", width=250, height=50, password=True, can_reveal_password=True
        )
    error_msg: ft.Text = ft.Text(
        "註冊失敗！", size=12, color="red", visible=False
    )
    button_register: ft.ElevatedButton = ft.ElevatedButton(
        text="註冊", width=250, height=50, on_click=lambda e: register_user(e)
        )
    page.add(
        Row(
            controls=[
                Column([
                    text_email,
                    text_username,
                    text_password,
                    error_msg,
                    button_register],
                    spacing=20
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


    def register_user(e: ft.ControlEvent):
        username = text_username.value
        password = text_password.value
        email = text_email.value

        try:
            register(email=email, password=password, username=username)
            page.controls.clear()
            from views.login_view import login_page
            login_page(page)
        except Exception as ex:
            print('Error: ', ex)
            error_msg.visible = True
            text_email.value = ""  # 清除電子郵件
            text_username.value = ""  # 清除使用者名稱
            text_password.value = ""  # 清除密碼
            text_email.focus()     # 重新聚焦到電子郵件輸入框
        finally:
            page.update()
