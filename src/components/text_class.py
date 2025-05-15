import flet as ft


class CustomText(ft.Text):
    def __init__(self, value: str, color:str, size:int):
        super().__init__(value, color, size)
        self.value = value
        self.color = color
        self.size = size
    
    def create_text(self):
        text = ft.Text(value=self.value, color=self.color, size=self.size)
        return text