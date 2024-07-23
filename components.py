import flet as ft

from functions import Functions
from flet_colors import Colors

class Components():
    def __init__(self,layout) -> None:
        #INSTANCES OF OTHER CLASSES
        self.functions=Functions(layout,self)
        self.colors= Colors()

        self.text_button_test=TextButton(
            text='Teste', icon= ft.icons.MOBILE_FRIENDLY, icon_color= self.colors.cor_teal,style=self.colors.button_black_amber,
            tooltip='Clique para testar botão', on_click_func=self.functions.test).text_button
        
        self.text_field_test=TextField(width=100, value='', label='TesteField', label_style=self.colors.text_green, on_change=self.functions.test,
                                       on_submit=self.functions.test, text_style=self.colors.text_black).text_field

class TextButton():
    def __init__(self, text, icon, icon_color, style, tooltip, on_click_func):
        self.text=text
        self.icon=icon
        self.icon_color=icon_color
        self.style=style
        self.tooltip=tooltip
        self.on_click_func=on_click_func

        self.create_text_button()
        
    def create_text_button(self):
        self.text_button= ft.TextButton(
            text=self.text,
            icon=self.icon, 
            icon_color= self.icon_color, 
            style= self.style, 
            tooltip= self.tooltip, 
            on_click= self.on_click_func
        )
    
class TextField():
    def __init__(self, width, value, label, label_style, on_change, on_submit, text_style):
        self.width= width
        self.value= value
        self.label= label
        self.label_style= label_style
        self.on_change= on_change
        self.on_submit= on_submit
        self.text_style= text_style

        self.create_text_field()

    def create_text_field(self):
        self.text_field=  ft.TextField(
            width=self.width,
            value=self.value,
            label= self.label,
            label_style=self.label_style,
            on_change=self.on_change,
            on_submit=self.on_submit,
            text_style=self.text_style
        )