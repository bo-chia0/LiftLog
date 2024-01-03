"""
Flet 會找到 main.py 作為程式的進入點
"""

import flet as ft
from views.login_view import login_page

def main(page: ft.Page):
    """
    redirect 至登入畫面
    """
    login_page(page)

if __name__ == "__main__":
    ft.app(target=main)
    