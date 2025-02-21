import config
import flet as ft

def main(page: ft.Page):

    config.configuracao(page)

    def alterar_tema (e):

        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
            btn_tema.tooltip = "Alterar para tema escuro"
            page.bgcolor = ft.Colors.WHITE

        else:
            page.theme_mode = ft.ThemeMode.DARK
            btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED
            btn_tema.tooltip = "Alterar para tema claro!"
            page.bgcolor = ft.Colors.GREY_900
        page.update()

    btn_tema = ft.IconButton(
        icon = ft.icons.WB_SUNNY_OUTLINED,
        tooltip = "Mudar tema", #cria uma pequena legenda
        on_click = alterar_tema

        
        )

    def adicionar(e):
        if not nova_tarefa.value:
            nova_tarefa.error_text = "Por favor, digite"
            page.update()

        else:
            nova_tarefa.error_text = None
            tarefa = ft.Row([])

            checkbox = ft.Checkbox(label = nova_tarefa.value)


            btn_remover = ft.IconButton(
                icon = ft.icons.DELETE_OUTLINED,        
                tooltip = "remover tarefa",
                on_click = lambda e: remover_tarefa(tarefa)    
                )
            
            tarefa.controls.extend([checkbox,btn_remover])

            page.add(tarefa)
            nova_tarefa.value = ""
            nova_tarefa.focus()
            nova_tarefa.update()

    def remover_tarefa(tarefa):
        page.controls.remove(tarefa)
        page.update()


    def saudacao(e):
        if not txt_nome.value:
            txt_nome.error_text = "Por favor, digite"
            page.update()
        else:
            nome = txt_nome.value
            #page.clean()
            page.add(ft.Text(f"Olá {nome}!"))

    txt_nome = ft.TextField(label="Seu nome?")
    nova_tarefa=ft.TextField(label="O que você deseja adicionar?", width=300)

    #label serve para subir o texto para ser substituido mas se manter visivel
    #hint_text serve para deixar o texto na caixa para ser substituido 

    page.add(ft.Row(
        [
            txt_nome,
            ft.ElevatedButton("Diga olá!", on_click=saudacao),
            btn_tema
        ]
    ))
    page.add(ft.Row(
        [
            nova_tarefa,
            ft.ElevatedButton("Adicionar", on_click=adicionar)
        ]
        ))

    def clicar(e):
        ...
        
    saida_texto = ft.Text()
    btn_submit=  ft.ElevatedButton(
        text='Enviar',
        on_click=clicar,
        disabled= True,

        bgcolor= ft.colors.GREEN,
        color= ft.colors.BLACK
    )
    cor_dropdown= ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option('Red'),
            ft.dropdown.Option('Green'),
            ft.dropdown.Option('Blue'),
            ft.dropdown.Option('Minha Opção')
        ]
    )

    page.add(saida_texto, btn_submit, cor_dropdown)

ft.app(main)