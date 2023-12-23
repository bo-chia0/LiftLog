"""
儲存重複出現的 components
"""
import flet as ft
from config import WIN_WIDTH, WIN_HEIGHT

# 頂部 header logo
header_logo = ft.Container(
    content=ft.Text(
        "LiftLog", size=35, weight=ft.FontWeight.W_900
    ),
    height=WIN_HEIGHT*0.1,
    alignment=ft.alignment.center,
    bgcolor=ft.colors.GREY_100,
)
