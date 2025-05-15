import flet as ft
from components.text_class import CustomText
from logic.edit_data import update_data
from config.database import db
from components.edit_modal import modal, group_category, group_method, input_amount




table = ft.DataTable(
    columns=[
        ft.DataColumn(label=CustomText('Fecha', 'white', size=20).create_text()),
        ft.DataColumn(label=CustomText('Categoria', 'white', size=20).create_text()),
        ft.DataColumn(label=CustomText('Pago', 'white', size=20).create_text()),
        ft.DataColumn(label=CustomText('Monto', 'white', size=20).create_text()),
        ft.DataColumn(label=CustomText('Acciones', 'white', size=20).create_text())
    ],
    rows=[],
    width=1200,
    heading_row_color='#131313',
)


def open_edit(e):
    modal.opacity = 1.0
    modal.update()
    try:
        row = db.get_data_for_id(e.control.data)
        for item in row:
            group_method.value = item['pago']
            group_category.value = item['categoria']
            input_amount.value = item['monto']
            input_amount.data = item['id']

            group_category.update()
            group_method.update()
            input_amount.update()

    except Exception as e:
        return str(e)

def delete_row(e):
    try:
        """IMPORTO LOS COMPONENTES DENTRO DE LA FUNCION PARA EVITAR IMPORTACION CIRCULAR"""
        from components.table import table, add_rows_table
        from components.header import total_data_sum
        db.delete_data(id=e.control.data)
        table.rows.clear()
        table.update()
        add_rows_table()
        total_data_sum()
        close_alert()
    except Exception as e:
        print(f'Error {e}')
    

def close_alert():
    alert.opacity = 0.0
    alert.visible = False
    alert.update()
    

def open_alert(e):
    alert.opacity = 1.0
    alert.visible = True
    alert.update()
    delete_button.data = e.control.data

delete_button = ft.ElevatedButton(
    'Confirmar', 
    color='white',
    bgcolor=ft.Colors.GREEN_500, 
    on_click=delete_row)

alert = ft.Container(
        content=ft.Column([
            ft.Text('Eliminar venta?', color='white', size=20),
            ft.Row([
                delete_button,
                ft.ElevatedButton('Salir', color='white', bgcolor=ft.Colors.RED_500, on_click=lambda _: close_alert())
            ])
        ]),
        opacity=0.0,
        animate=ft.Animation(300, curve='easeIn'),
        width=200,
        height=120,
        margin=ft.Margin(500,250,0,0),
        bgcolor='#2c2c2c',
        padding=ft.Padding(30,20,0,0),
        border_radius=ft.BorderRadius(20,20,20,20),
        visible=False,
        shadow=ft.BoxShadow(5, 50, color=ft.Colors.BLACK)
        
    )

def add_rows_table():
    table.rows.clear()
    row = db.get_all_data()
    for item in row:
        rows = ft.DataRow(
            cells=[
                ft.DataCell(content=ft.Text(value=item['fecha'],color='white')),
                ft.DataCell(content=ft.Text(value=item['categoria'],color='white')),
                ft.DataCell(content=ft.Text(value=item['pago'],color='white')),
                ft.DataCell(content=ft.Text(value=f'$ {item['monto'] or 0:,.0f}'.replace(",", "X").replace(".", ",").replace("X", "."), color='white')),
                ft.DataCell(content=ft.Row(
                    controls=[
                        ft.IconButton(
                            ft.Icons.EDIT, 
                            icon_color='white', 
                            on_click=open_edit, 
                            data=item['id'],
                            bgcolor=ft.Colors.BLUE_500),
                        ft.IconButton(
                            ft.Icons.DELETE, 
                            icon_color='white', 
                            bgcolor=ft.Colors.RED_500, 
                            on_click=open_alert, 
                            data=item['id'])
                    ]
                ))
            ]
        )
        table.rows.append(rows)
    table.update()




       