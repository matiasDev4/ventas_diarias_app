import flet as ft


snack = ft.SnackBar(content=ft.Text(''))

def snack_message(message: str , color , open: bool):
    snack.content = ft.Text(message, color='white', size=15)
    snack.bgcolor = color
    snack.open = open
    snack.update()
