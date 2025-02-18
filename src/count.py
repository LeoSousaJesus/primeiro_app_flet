import flet as ft

def main(page: ft.Page):
    page.title = 'Primeiro app flet'
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    num1 = ft.TextField(value='0', text_align=ft.TextAlign.RIGHT)

    def alterar_tema (e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema escuro'
            page.bgcolor = ft.colors.WHITE
          

        else:
            page.theme_mode = ft.ThemeMode.DARK
            btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema claro'
            page.bgcolor = ft.colors.BLACK
       
        page.update()

    btn_tema = ft.IconButton(
        icon=ft.icons.WB_SUNNY_OUTLINED,
        tooltip='Alterar o tema',
        on_click=alterar_tema
    )
    
    def menos(e):
        num1.value = str(int(num1.value) - 1)
        page.update()
        
    def mais(e):
        num1.values = str(int(num1.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [

                ft.IconButton(ft.icons.ADD, on_click=mais),
                num1,
                ft.IconButton(ft.icons.REMOVE, on_click=menos),
                btn_tema

            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


    page.add(num1)
ft.app(main)