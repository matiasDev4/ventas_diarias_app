import flet as ft
from components.form import form
from components.header import header, total_data_sum
from components.table import add_rows_table, table, alert
from components.edit_modal import modal
from components.snack_message import snack
from config.database import db


def main(page: ft.Page):
    page.window.width = 1200
    page.window.height = 700
    page.window.resizable = False
    page.window.maximizable = False
    page.window.alignment = ft.Alignment(0,0)
    page.bgcolor = '#1c1c1c'
    page.padding = ft.Padding(0,0,0,0)
    
    def app_close(e):
        db.close()

    page.window.on_event = app_close

    container = ft.Stack(
        controls=[
            ft.Container(
            content=ft.Column(
            controls=[
                header,
                form(page),
                ft.Container(ft.Column([table], scroll=ft.ScrollMode.ALWAYS), height=400)  
            ]
                
            ),
            height=700,
            padding=ft.Padding(0,0,0,0),
            margin=ft.Margin(0,0,0,0)
    ),
    modal,
    alert,
    snack
    
        ]
    )
    
    page.add(container)
    add_rows_table()
    total_data_sum()
    

    
    
    
    


if __name__ == '__main__':
    ft.app(
        target=main,
        assets_dir='src/assets',
        view=ft.AppView.FLET_APP
    )