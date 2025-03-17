import flet as ft


class Home(ft.View):
    def __init__(self):
        data = "Home Data"
        controls = [
            ft.AppBar(title=ft.Text("Top view"), bgcolor=ft.colors.SURFACE_VARIANT),
        ]
        super().__init__("/", controls=controls)
        self.data = data
