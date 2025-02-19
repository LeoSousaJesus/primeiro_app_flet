import flet as ft


def configuracao(page: ft.Page):
    page.window.max_height = 500
    page.window.width = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    

