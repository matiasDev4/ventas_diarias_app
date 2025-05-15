from config.database import db

def update_data(categoria: str, pago:str, monto:int, id: int):
    try:
        new_data = {
        'categoria': categoria,
        'pago': pago,
        'monto': monto,
        }
        db.update_data(new_data, id)
    except Exception as e:
        return str(e)