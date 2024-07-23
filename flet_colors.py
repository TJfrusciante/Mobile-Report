import flet as ft

class Colors():
    def __init__(self) -> None:
        #Text colors
        self.text_black= ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)
        self.text_green=ft.TextStyle(color=ft.colors.GREEN, weight=ft.FontWeight.BOLD)
        self.text_red=ft.TextStyle(color=ft.colors.RED, weight=ft.FontWeight.BOLD)
        self.text_teal=ft.TextStyle(color=ft.colors.TEAL, weight=ft.FontWeight.W_500)
        self.text_invisible_label_style = ft.TextStyle(color=ft.colors.TRANSPARENT)
        #Colors
        self.cor_black=ft.colors.BLACK
        self.cor_teal=ft.colors.TEAL
        self.cor_amber=ft.colors.AMBER
        self.cor_red=ft.colors.RED
        self.cor_green=ft.colors.GREEN
        self.cor_blue=ft.colors.BLUE
        self.cor_white=ft.colors.WHITE
        self.cor_orange=ft.colors.ORANGE
        self.cor_yellow=ft.colors.YELLOW
        #Hex colors
        self.persian_green_hex='#00a693'
        self.salmon_hex='#FA8072'
        self.silver_hex='#C0C0C0'
        self.black_hex='#000000'
        self.lime_hex='#00FF00'
        self.yellow_hex='#FFFF00'
        self.aqua_hex='#00FFFF'
        self.teal_hex='#008080'
        self.purple_hex='#800080'
        self.orange_red_hex='#FF4500'
        self.orange_hex='#FF8C00'
        self.dark_gray_hex='#2F4F4F'
        self.blue_hex='#1E90FF'
        self.pink_hex='#FF69B4'
        #Text button styles
        self.button_black_amber=ft.ButtonStyle(color={
                                        ft.MaterialState.DEFAULT: self.cor_black,
                                        ft.MaterialState.HOVERED: self.cor_amber
                                    })