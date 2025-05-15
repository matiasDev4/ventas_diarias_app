import flet as ft
from components.text_class import CustomText
from config.database import db
from datetime import datetime
from components.table import add_rows_table, table
from components.header import total_data_sum
from components.snack_message import snack_message

def form(page):
    radio_options = [{
        'label': 'Cigarrillo',
    },
    {
        'label': 'Varios',
    },
    {
        'label': 'Impresiones',
    },
    {
        'label': 'Libreria',
    }]

    radio_methods_pay = [{
        'label': 'Efectivo',
    },
    {
        'label': 'Transferencia',
    }]

    def submit_data(e):
        if group_category.value == '' or group_method_pay.value == '' or input_amount.value == '':
            snack_message(message='Datos vacios', color=ft.Colors.RED_500, open=True)
        else:
            data = {
                'fecha': datetime.now().strftime('%d-%m-%Y'),
                'categoria': group_category.value,
                'pago': group_method_pay.value,
                'monto': input_amount.value
            }
            db.add_data(data=data)
            add_rows_table()
            total_data_sum()
            group_category.value = ''
            group_method_pay.value = ''
            input_amount.value = ''
            group_category.update()
            group_method_pay.update()
            input_amount.update()
            snack_message(message='Venta creada!', color=ft.Colors.GREEN_500, open=True)

    group_category = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(
                    label=x['label'], 
                    value=x['label'], 
                    label_style=ft.TextStyle(color='white'),
                    active_color=ft.Colors.GREEN_400,
                    hover_color=ft.Colors.BLUE_GREY_800) for x in radio_options]
        )
    )

    group_method_pay = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(
                    label=x['label'], 
                    value=x['label'], 
                    label_style=ft.TextStyle(color='white'), 
                    active_color=ft.Colors.GREEN_400) for x in radio_methods_pay]
        )
    )

    input_amount = ft.TextField(
                    label='Ingresar monto',
                    label_style=ft.TextStyle(color='white'),
                    width=200,
                    border_color='white',
                    on_submit=submit_data,
                    color='white'
                    
                )

    content = ft.Container(
        content=ft.Column(
            controls=[
                group_category,
                group_method_pay,
                input_amount
            ]
        ),
        padding=ft.Padding(10,20,10,20)
    )
    return content