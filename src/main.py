import flet as ft


def main(page: ft.Page):
    page.appbar = ft.AppBar(
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        title=ft.Text("MHWRecipe"),
    )
    page.bottom_appbar = ft.BottomAppBar(bgcolor=ft.Colors.BLUE)
    page.add(
        ft.Text("main!"),
        ft.CupertinoFilledButton(
            content=ft.Text("CupertinoFilled"),
            opacity_on_click=0.3,
            on_click=lambda e: print("CupertinoFilledButton clicked!"),
        ),
    )


ft.app(main)
