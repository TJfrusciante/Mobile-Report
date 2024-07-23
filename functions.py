import flet as ft

from flet_colors import Colors
from data_base import DataBase

class Functions():
    def __init__(self, layout, components) -> None:
        self.layout=layout
        self.components=components
        #INTANCES
        self.data_base=DataBase()
        self.colors=Colors()
    
    def test(self, e):
        print('testando com sucesso!')