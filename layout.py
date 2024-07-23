
import flet as ft
from flet_colors import Colors
from components import Components

class Layout():
    def __init__(self, page) -> None:
        self.colors=Colors()

        self.page=page
        self.page.title='Mobile Report'
        self.page.bgcolor=self.colors.cor_black
        self.page.padding= ft.padding.all(10)
        self.page.theme=ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=self.colors.cor_black,#primários, exemplo: cancelar/confirmar/ok
                on_primary=self.colors.cor_white,#cor dentro dos primarys, exemplo: número dentro da data selecionada no DatePicker
                on_surface=self.colors.cor_black,#cor de coisas na superficie, exemplo: datas no DatePicker
                surface=self.colors.cor_amber,#cor das superficies, exemplo: cor de fundo do DatePicker
                surface_tint=self.colors.cor_green,#cor de alertDialog outerborder
                on_surface_variant=self.colors.cor_black,#cor de checkBox box border
                
                )
            )
        
        #INTANCES OF OTHER CLASSES
        self.components=Components(self)

        #HEADER
        self.row_header=ft.Row(
            controls= [
                self.components.text_field_test
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.container_header= ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[self.colors.cor_amber,self.colors.cor_yellow]
            ),
            content=self.row_header
        )
        #BODY
        self.body_container=ft.Column(
            width=4000,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            controls=[
                self.components.text_button_test
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.container_main=ft.Container(
            expand=True,
            content=self.body_container,
             gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[self.colors.cor_amber,self.colors.cor_yellow]
                ),
                padding=10,
        )
        #FOOTER
        self.row_footer=ft.Row(
            controls= [
                self.components.text_field_test
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.container_footer= ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[self.colors.cor_amber,self.colors.cor_yellow]
            ),
            content=self.row_header
        )
        #B
        #LAYOUT THAT'S ADDED ON THE SCREEN
        self.full_layout=ft.Column(
        expand=True,
        controls=[
            self.container_header,
            self.container_main,
            self.container_footer
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        self.page.add(self.full_layout)

        self.update_page()
    def add_to_page(self, item_to_add):
        self.page.add(item_to_add)

    def update_page(self):
        self.page.update()

