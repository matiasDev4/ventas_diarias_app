import flet as ft
from logic.edit_data import update_data
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


def close_modal(e):
    modal.opacity = 0.0
    modal.update()


def submit_update(e):
    """IMPORTO LOS COMPONENTES DENTRO DE LA FUNCION PARA EVITAR EL ERROR DE IMPORTACION CIRCULAR"""
    from components.table import table, add_rows_table
    from components.header import total_data_sum
    update_data(group_category.value, group_method.value, input_amount.value, e.control.data)
    table.rows.clear()
    table.update()
    add_rows_table()
    total_data_sum()
    modal.opacity = 0.0
    modal.update()
    


group_category = ft.RadioGroup(
    ft.Row(
        controls=[
            ft.Radio(
                label=item['label'], 
                value=item['label'],
                label_style=ft.TextStyle(color='white'),
                active_color=ft.Colors.GREEN_400) for item in radio_options
        ]
    )
)

group_method = ft.RadioGroup(
    ft.Row(
        controls=[
            ft.Radio(
                label=item['label'], 
                value=item['label'],
                label_style=ft.TextStyle(color='white'),
                active_color=ft.Colors.GREEN_400) for item in radio_methods_pay]
    )
)

input_amount = ft.TextField(
                label='Ingresar monto',
                label_style=ft.TextStyle(color='white'),
                width=200,
                border_color='white', 
                on_submit=submit_update,
                color='white'
                )

form = ft.Column(
    controls=[
        ft.Container(
                    ft.Row(
            controls=[
                ft.Text('Editar ventas', size=20, color='white'),
                ft.IconButton(
                    ft.Icons.CLOSE, 
                    icon_color='white', 
                    bgcolor=ft.Colors.RED_600, 
                    icon_size=20, on_click=close_modal)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),padding=ft.Padding(10, 10, 10, 20)
        ),
        group_category,
        group_method,
        input_amount 
    ]
)

modal = ft.Container(
    content=form,
    opacity=0.0,
    animate_opacity=ft.Animation(300, curve='easeInOut'),
    bgcolor='#2c2c2c',
    height=300,
    width=450,
    margin=ft.Margin(400, 200, 20, 20),
    padding=ft.Padding(20,20,10,0),
    border_radius=ft.BorderRadius(20,20,20,20),
    shadow=ft.BoxShadow(5, 50, color=ft.Colors.BLACK)
)
