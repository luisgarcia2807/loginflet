import flet as ft

def main(page: ft.Page):
    page.title = "Interfaz con Barra de Tareas Animada"
    page.window_width = 450
    page.window_height = 600
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Funciones para cambiar de contenedor
    def show_container1(e):
        contenedor_actual.content = c1
        contenedor_actual.update()

    def show_container2(e):
        contenedor_actual.content = c2
        contenedor_actual.update()

    def show_container3(e):
        contenedor_actual.content = c3
        contenedor_actual.update()

    # Contenedor principal
    c1 = ft.Container(
        content=ft.Text("Este es el Contenedor 1", size=30),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.RED_100,
        expand=True,
        padding=ft.padding.all(20),
        border_radius=15,
    )

    c2 = ft.Container(
        content=ft.Text("Este es el Contenedor 2", size=30),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREEN_100,
        expand=True,
        padding=ft.padding.all(20),
        border_radius=15,
    )

    # Nueva interfaz con barra de tareas animada (Contenedor 3)
    def on_button_click(e):
        for icon_button in icon_buttons:
            if icon_button.icon == e.control.icon:
                icon_button.scale = 1.2
                icon_button.rotate = 0.3
                icon_button.update()
            else:
                icon_button.scale = 1.0
                icon_button.rotate = 0.0
                icon_button.update()

        content_area.content.value = f"Button '{e.control.icon}' clicked!"
        content_area.update()

    content_area = ft.Container(
        content=ft.Text("Este es el contenido principal", size=30),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLUE_100,
        expand=True,
        padding=ft.padding.all(20),
        border_radius=15,
    )

    icon_buttons = [
        ft.IconButton(icon=ft.icons.HOME, on_click=on_button_click, animate_scale=ft.Animation(300, "easeInOut"), animate_rotation=ft.Animation(300, "easeInOut")),
        ft.IconButton(icon=ft.icons.SETTINGS, on_click=on_button_click, animate_scale=ft.Animation(300, "easeInOut"), animate_rotation=ft.Animation(300, "easeInOut")),
        ft.IconButton(icon=ft.icons.PERSON, on_click=on_button_click, animate_scale=ft.Animation(300, "easeInOut"), animate_rotation=ft.Animation(300, "easeInOut")),
        ft.IconButton(icon=ft.icons.NOTE, on_click=on_button_click, animate_scale=ft.Animation(300, "easeInOut"), animate_rotation=ft.Animation(300, "easeInOut")),
        ft.IconButton(icon=ft.icons.MESSAGE, on_click=on_button_click, animate_scale=ft.Animation(300, "easeInOut"), animate_rotation=ft.Animation(300, "easeInOut")),
    ]

    taskbar = ft.Container(
        content=ft.Row(
            icon_buttons,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        ),
        bgcolor=ft.colors.GREY_200,
        padding=ft.padding.symmetric(vertical=10),
    )

    c3 = ft.Column(
        [
            content_area,
            taskbar,
        ],
        expand=True,
        spacing=0,
    )

    contenedor_actual = ft.Container(content=c1, expand=True)

    # Botones para cambiar de contenedor
    button1 = ft.ElevatedButton(text="Mostrar Contenedor 1", on_click=show_container1)
    button2 = ft.ElevatedButton(text="Mostrar Contenedor 2", on_click=show_container2)
    button3 = ft.ElevatedButton(text="Mostrar Contenedor 3", on_click=show_container3)

    page.add(
        ft.Column(
            [
                contenedor_actual,
                ft.Row([button1, button2, button3], alignment=ft.MainAxisAlignment.CENTER)
            ],
            expand=True,
        )
    )

ft.app(target=main)
