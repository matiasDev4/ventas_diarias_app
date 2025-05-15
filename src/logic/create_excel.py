import pandas as pd
import os
import xlsxwriter

def create_excel(data: dict, path):
    try:
        workbook = xlsxwriter.Workbook(path)
        workbook.add_worksheet()
        workbook.close()
        new_df = pd.DataFrame(data=data)
        if os.path.exists(path):
            exist = pd.read_excel(path)
            print(exist)
            df2 = pd.concat([exist, new_df], ignore_index=True)
        else:
            df2 = new_df
        df2.to_excel(path, index=False) 
        print('Archivo creado!')
    except Exception as e:
        print(f'Error: {e}')