import flet as ft

from layout import Layout

class MobileApp():
    def __init__(self, page= ft.Page) -> None:
        Layout(page)
        

if __name__=='__main__':
    ft.app(target=MobileApp)