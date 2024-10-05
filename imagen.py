import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo de Imágenes"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50

    # Carga una imagen desde una URL o archivo local
    img = ft.Image(
        src="TDAH-ADULTOS.jpeg",  # Ruta a la imagen (puedes cambiarla)
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    # Crea un contenedor para las imágenes
    images = ft.Row(expand=1, wrap=False, scroll="always")
    page.add(img, images)

    

ft.app(target=main)
