import flet as ft
from config.database import db
from logic.create_excel import create_excel
from pathlib import Path
from datetime import datetime
import xlsxwriter
from components.table import add_rows_table
from components.snack_message import snack_message

total_text = ft.Text(value=f'$ {0}', color='white', size=20)
total_transfer = ft.Text(value=f'$ {0}', color='white', size=20)
total_efectivo = ft.Text(value=f'$ {0}', color='white', size=20)


def submit_day(e):
    data = {
        'fecha': datetime.now().strftime('%d-%m-%Y'),
        'total': total_text.value,
        'efectivo': total_efectivo.value,
        'virtual': total_transfer.value
    }
    db.save_day_sales(data)
    save_excel()

def save_excel():
    try:
        excel = Path.home() / 'Desktop'
        if not excel.exists():
            excel = Path.home() / 'Escritorio'
        create_folder = Path(excel) / 'ventas excel'
        create_folder.mkdir(parents=True, exist_ok=True)
        path = create_folder / 'ventas.xlsx'
        row = db.get_totales()
        for item in row:
            data = {
                'fecha': [item['fecha']],
                'total': [item['total']],
                'efectivo': [item['total_efectivo']],
                'virtual':[item['total_virtual']]
            }
            create_excel(data, path)
        db.delete_all_data()
        add_rows_table()
        total_data_sum()
        snack_message(message='Datos guardados!', color=ft.Colors.GREEN_500, open=True)
    except Exception as e:
        snack_message(message='Error al guardar archivo excel', color=ft.Colors.RED_500, open=True)
    
header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Row([ft.Text(value='Total de ventas', size=20, color='white'),
                        total_text], ),
                        ft.Row([ft.Text(value='Efectivo', size=20, color='white'),
                        total_efectivo]),
                        ft.Row([ft.Text(value='Virtual', size=20, color='white'),
                        total_transfer])
                    ],spacing=100
                ),
                ft.ElevatedButton(
                    text='Nuevo dia',
                    bgcolor=ft.Colors.GREEN_600,
                    color='white',
                    on_click=submit_day,
                    tooltip='Crea un nuevo dia y guarda los datos en excel'
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            
        ),
        padding=ft.Padding(10,0,10,0),
        bgcolor='#131313',
        height=60
    )

def total_data_sum():
    total = db.sum_mont_data()
    efectivo = db.sum_total_cash()
    transfer = db.sum_total_tranfer()
    total_text.value = f'$ {total[0]['total'] or  0:,.0f}'.replace(",", "X").replace(".", ",").replace("X", ".")
    total_efectivo.value = f'$ {efectivo[0]['total_efectivo'] or  0:,.0f}'.replace(",", "X").replace(".", ",").replace("X", ".")
    total_transfer.value = f'$ {transfer[0]['total_tranfer'] or  0:,.0f}'.replace(",", "X").replace(".", ",").replace("X", ".")
    total_efectivo.update()
    total_transfer.update()
    total_text.update()