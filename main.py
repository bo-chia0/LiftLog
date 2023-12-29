"""
This is the entry point for your Flet application.
Here, you would set up your Flet app and tie together the views and services.
"""

import flet as ft
from views.login_view import login_page
from views.home_view import home_page

def main(page: ft.Page):
    """
    redirect 至登入畫面
    """
    login_page(page)

if __name__ == "__main__":
    ft.app(target=main)
    