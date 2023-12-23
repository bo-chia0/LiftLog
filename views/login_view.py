"""
這個檔案負責登入畫面的呈現
"""
import flet as ft
from flet import Row, Column
from flet_core.control_event import ControlEvent
from config import WIN_WIDTH, WIN_HEIGHT, CURRENT_USER_ID
from controllers.account_controllers import login

def login_page(page: ft.Page):
    """
    登入畫面
    """
    # window properties
    page.title = "Login"
    page.window_width = WIN_WIDTH
    page.window_height = WIN_HEIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # elements
    text_email: ft.TextField = ft.TextField(
        label="電子郵件", width=250, height=50
        )
    text_password: ft.TextField = ft.TextField(
        label="密碼", width=250, height=50, password=True, can_reveal_password=True
        )
    error_msg: ft.Text = ft.Text(
        "登入失敗！", size=12, color="red", visible=False
    )
    button_login: ft.ElevatedButton = ft.ElevatedButton(
        text="登入", width=250, height=50, on_click=lambda e: login_user(e)
        )
    button_register: ft.ElevatedButton = ft.ElevatedButton(
        text="註冊", width=250, height=50, on_click=lambda e: navigate_to_register_page(page)
    )
    page.add(
        Row(
            controls=[
                Column([
                    text_email,
                    text_password,
                    error_msg,
                    button_login,
                    button_register],
                    spacing=20
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    def login_user(e: ControlEvent):
        email = text_email.value
        password = text_password.value

        try:
            user = login(email, password)
            if user is not None:
                global CURRENT_USER_ID 
                CURRENT_USER_ID = user.id
                page.controls.clear()
                from views.home_view import home_page
                home_page(page)
            else:
                raise Exception("帳號或密碼錯誤")
        except Exception as ex:
            error_msg.value = "登入失敗: " + str(ex)
            error_msg.visible = True
            text_email.value = ""  # 清除電子郵件
            text_password.value = ""  # 清除密碼
            text_email.focus()     # 重新聚焦到電子郵件輸入框
        finally:
            page.update()

    def navigate_to_register_page(page: ft.Page):
        from views.register_view import register_page
        page.controls.clear()  # 清除當前頁面的元素
        register_page(page)    # 調用呈現註冊頁面的函數
