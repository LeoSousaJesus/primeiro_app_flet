import flet as ft

def main(page: ft.Page):

    #config janela
    page.title = 'configuração de pagina'
    #page.bgcolor = ft.Colors.BLACK26
    page.theme_mode = ft.ThemeMode.DARK

    def alterar_tema (e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema escuro'
            page.bgcolor = ft.colors.WHITE
            t.bgcolor = ft.colors.BLACK
            t.color = ft.colors.WHITE

        else:
            page.theme_mode = ft.ThemeMode.DARK
            btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema claro'
            page.bgcolor = ft.colors.BLACK
            t.bgcolor = ft.colors.WHITE
            t.color = ft.colors.BLACK
        page.update()

    btn_tema = ft.IconButton(
        icon=ft.icons.WB_SUNNY_OUTLINED,
        tooltip='Alterar o tema',
        on_click=alterar_tema
    )

    #tamanho da janela
    #page.window.width = 500 #largura
    #page.window.height = 800 #altura

    #alinhamento
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.padding = ft.padding.all(100)
    page.padding = ft.padding.only(top=10, left=20, right=50, bottom=10)
    page.spacing = 100
    page.window.always_on_top = False #para manter em primeiro plano
    page.window.title_bar_hidden = False #para remover a barra de menu
    page.window.frameless = False #para remover botões
    page.window.full_screen = False #para poder manter em tela cheia
    
    #limitar tamanhos de tela
    page.window.max_height = 500 #para alterar o tamanho maximo da tela
    page.window.min_height = 500 #para alterar o tamanho minimo da tela
    page.window.max_width = 600
    page.window.min_width = 600

    page.window.resizable = False

    def janela_evento(e):
        match e.data:
            case 'moved':
                print('moveu a pagina')
            case 'resized':
                print('Redimencionou a pagina')
            case 'minimize':
                print('Minimizou a pagina')
            case 'Maximize':
                print('Maximizou a pagina')
    
    #bloco de texto
    t = ft.Text(
        value= 'Um preto meio branco', 
        color= ft.colors.RED_200, 
        size=80,
        italic=True,
        weight= 'bold', #ft.fontweight.BOLD
        bgcolor= ft.Colors.BROWN,
        font_family= 'verdana'
         )
    
    elementos = [
        ft.Text(value='Text1', size=20, bgcolor=ft.Colors.PURPLE),
        ft.Text(value='Text2', size=20, bgcolor=ft.Colors.GREEN),
        ft.Text(value='Text3', size=20, bgcolor=ft.Colors.BLUE),
        ft.Text(value='Text4', size=20, bgcolor=ft.Colors.RED)
    ]

    #page.update()
    page.add(*elementos, t, btn_tema)

ft.app(main)
