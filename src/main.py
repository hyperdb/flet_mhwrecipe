import flet as ft


def main(page: ft.Page):
    page.appbar = ft.AppBar(
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        title=ft.Text("MHWRecipe"),
    )
    page.bottom_appbar = ft.BottomAppBar(bgcolor=ft.Colors.BLUE)
    page.add(ft.Text("main!"))


ft.app(main)
