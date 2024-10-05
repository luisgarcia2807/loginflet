import flet as ft
from babel.dates import format_date
import re
from datetime import datetime
import preuba

def main(page: ft.Page):
    page.padding = 0
    page.window_width = 450
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    myicons = ["home", "create", "person", "settings", "favorite", "grade", "shopping_cart_checkout", "expand_circle_down"]
    

    def youchange(e):
        pass

    def youtaphere(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("Open your dialog", size=30),
            content=ft.Text("this sample"),
            actions=[
                ft.ElevatedButton("Close"),
                ft.ElevatedButton("test")
            ],
        )

    t = ft.Tabs(
        selected_index=0,
        animation_duration=100,
        indicator_color="white",
        divider_color="blue",
        scrollable=True,
        on_change=youchange,
        tabs=[]
    )

    for x in myicons:
        t.tabs.append(
            ft.Tab(
                tab_content=ft.Icon(
                    name=x,
                    size=40,
                    color="white",
                )
            )
        )
    def switch_to_container1(e):
        c.content = c1
        page.update()

    def switch_to_container2(e):
        c.content = c2
        page.update()

    def switch_to_container3(e):
        c.content = c3
        page.update()

    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()
        return c.content

    # Variables para guardar los datos
    email_login = ft.TextField(
        width=280,
        height=40,
        hint_text='Correo Electronico',
        border='underline',
        color='black',
        prefix_icon=ft.icons.EMAIL,
    )

    password_login = ft.TextField(
        width=280,
        height=40,
        hint_text='Contraseña',
        border='underline',
        color='black',
        prefix_icon=ft.icons.LOCK,
        password=True,
    )

    email_register = ft.TextField(
        width=280,
        height=60,
        hint_text='Correo Electronico',
        border='underline',
        color='black',
        prefix_icon=ft.icons.EMAIL,
        max_length=30,
    )

    password_register = ft.TextField(
        width=280,
        height=60,
        hint_text='Contraseña',
        border='underline',
        color='black',
        prefix_icon=ft.icons.LOCK,
        password=True,
        max_length=20,
    )

    name_register = ft.TextField(
        width=140,
        height=80,
        max_length=20,
        hint_text='Nombre',
        border='underline',
        color='black',
        prefix_icon=ft.icons.PERM_CONTACT_CAL,
        input_filter= ft.TextOnlyInputFilter(),
    )

    apellido_register = ft.TextField(
        width=140,
        height=80,
        hint_text='Apellido',
        border='underline',
        color='black',
        prefix_icon=ft.icons.PERM_CONTACT_CAL,
        input_filter= ft.TextOnlyInputFilter(),
        max_length=20,
    )

    birthdate = None  # Variable para almacenar la fecha de nacimiento

    def date_change(e):
        nonlocal birthdate
        birthdate = e.control.value
        formatted_date = format_date(birthdate, format='full', locale='es')
        page.controls.append(ft.Text(f"Fecha seleccionada: {formatted_date}"))
        page.update()

    date_input = ft.DatePicker(on_change=date_change)
    page.overlay.append(date_input)

    # Dropdown for selecting country
    country_dropdown = ft.Dropdown(
        width=280,
        height=40,
        hint_text="Seleccione su país",
        border='underline',
        options=[
            ft.dropdown.Option("Argentina"),
            ft.dropdown.Option("Bolivia"),
            ft.dropdown.Option("Brasil"),
            ft.dropdown.Option("Chile"),
            ft.dropdown.Option("Colombia"),
            ft.dropdown.Option("Ecuador"),
            ft.dropdown.Option("Paraguay"),
            ft.dropdown.Option("Peru"),
            ft.dropdown.Option("Uruguay"),
            ft.dropdown.Option("Venezuela"),
        ]
    )
    thad_dropdown = ft.Dropdown(
        width=280,
        height=40,
        hint_text="Selecione su tipo de TDAH",
        border='underline',
        options=[
            ft.dropdown.Option("Falta de atencion predominante"),
            ft.dropdown.Option("Conducta hiperativa/impulsiva"),
            ft.dropdown.Option("Combinado"),
        ]
    )
    Genero_dropdown = ft.Dropdown(
        width=280,
        height=40,
        hint_text="Selecione su Genero",
        border='underline',
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Femenino"),
            ft.dropdown.Option("Prefiero no decirlo"),
        ]
    )

    def iniciar_sesion(e):
        email = email_login.value
        password = password_login.value
        incorreo,num=verificar_correo(email)
        print(num)

        if not email or not password:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Por favor, complete todos los campos."),
                actions=[
                    ft.ElevatedButton("OK", on_click=close_dialog)
                ],
                open=True
            )
        elif incorreo== True:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("El correo no  esta registrado"),
                actions=[
                    ft.ElevatedButton("OK", on_click=close_dialog)
                ],
                open=True
            )
        elif vereficar_contrasena(password,num)== False:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Contraseña incorrecta"),
                actions=[
                    ft.ElevatedButton("OK", on_click=close_dialog)
                ],
                open=True
            )
        else:
            
            c.content = c3
            page.update()
            
        
        
        page.update()
        return


    
    def validar_correo(correo):
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(patron, correo) is not None
    
    def convertir_pais(pais_str):
        if pais_str=="Argentina":
            return 1
        if pais_str=="Bolivia":
            return 2
        if pais_str=="Brasil":
            return 3
        if pais_str=="Chile":
            return 4
        if pais_str=="Colombia":
            return 5
        if pais_str=="Ecuador":
            return 6
        if pais_str=="Paraguay":
            return 7
        if pais_str=="Peru":
            return 8
        if pais_str=="Uruguay":
            return 9
        if pais_str=="Venezuela":
            return 10
        
    def convertir_tdah(tdah_str):
        if tdah_str=="Falta de atencion predominante":
            return 1
        if tdah_str=="Conducta hiperativa/impulsiva":
            return 2
        if tdah_str=="Combinado":
            return 3
    
    def convertir_fecha(fecha_str):
    # Diccionario para mapear los nombres de los meses en español a números
        meses = {
            "enero": "01",
            "febrero": "02",
            "marzo": "03",
            "abril": "04",
            "mayo": "05",
            "junio": "06",
            "julio": "07",
            "agosto": "08",
            "septiembre": "09",
            "octubre": "10",
            "noviembre": "11",
            "diciembre": "12"
        }
        partes = fecha_str.split(", ")[1].split(" de ")
        dia = partes[0]
        mes = meses[partes[1]]
        año = partes[2]

        fecha_numerica = f"{año}/{mes}/{dia.zfill(2)}"

        return fecha_numerica
    
    def verificar_correo (correo_str):
        resgitrocorreo=preuba.mostrar(1)
        inco= True
        j=0
        y=-1
        for x in resgitrocorreo:
            if correo_str==x[3]:
                inco=False
                y=j
            j+=1
        return inco,y
    
    def vereficar_contrasena(contrasena_str,num):
        registrocorreo=preuba.mostrar(1)
        if registrocorreo[num][4]==contrasena_str:
            return True
        return False
        


    def validar_contrasena(contrasena):
        # Criterios de validación
        longitud_minima = 8
        tiene_letra = re.search(r'[a-zA-Z]', contrasena) is not None
        tiene_numero = re.search(r'\d', contrasena) is not None
        tiene_caracter_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena) is not None
        tiene_espacio = re.search(r'\s', contrasena) is not None

        if len(contrasena) < longitud_minima:
            return False, "La contraseña debe tener al menos 8 caracteres."
        if not tiene_letra:
            return False, "La contraseña debe tener al menos una letra."
        if not tiene_numero:
            return False, "La contraseña debe tener al menos un número."
        if not tiene_caracter_especial:
            return False, "La contraseña debe tener al menos un carácter especial."
        if tiene_espacio:
            return False, "La contraseña no debe contener espacios."

        return True, "Contraseña válida."
    
    
    

    def registrarse(e):
        name = name_register.value
        apellido = apellido_register.value
        email = email_register.value
        password = password_register.value
        selected_country = country_dropdown.value
        selected_tdah = thad_dropdown.value
        selected_genero = Genero_dropdown.value
        formatted_birthdate = format_date(birthdate, format='full', locale='es') 

        
        inpassword,mensajepassword=validar_contrasena(password)
        inpais=convertir_pais(selected_country)
        intdah=convertir_tdah(selected_tdah)
        incorreo,num=verificar_correo(email)

        formatted_birthdate= convertir_fecha(formatted_birthdate)
        
        if not name or not apellido or not email or not password or not selected_country or not selected_tdah or not selected_genero or not formatted_birthdate:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Por favor, complete todos los campos."),
                actions=[
                    ft.ElevatedButton("OK", on_click=close_dialog)
                ],
                open=True
            )
        elif validar_correo(email)== False:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Correo invalido."),
                actions=[
                    ft.ElevatedButton("OK", on_click=close_dialog)
                ],
                open=True
            )
        elif incorreo== False:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Correo ya existe.\n No puede ser usado para el registro"),
                actions=[
                    ft.ElevatedButton("OK", on_click=close_dialog)
                ],
                open=True
            )
        elif inpassword == False:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text(F"{mensajepassword}."),
                actions=[
                    ft.ElevatedButton("OK", on_click=close_dialog)
                ],
                open=True
            )

        else:
            # Mostrar los valores en un cuadro de diálogo
            page.dialog = ft.AlertDialog(
                title=ft.Text("Información ingresada"),
                content=ft.Text(f"Nombre: {name}\nApellido: {apellido}\nCorreo: {email}\nContraseña: {password}\nFecha de Nacimiento: {formatted_birthdate}\nPaís: {selected_country}\nSu tipo de tdha: {selected_tdah}\nSu genero es: {selected_genero}"),
                actions=[
                    ft.TextButton("OK", on_click=close_dialog)
                ],
                open=True
            ) 
            preuba.insertar(name,apellido,email,password, inpais, intdah,selected_genero,formatted_birthdate)
            c.content = c3
            page.update()
            
        
           
        page.update()
        

        
    
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    c1 = ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        'Iniciar Sesion',
                        width=360,
                        size=30,
                        weight='w900',
                        text_align='center',
                        color="blue"
                    ),
                    ft.Container(
                        content=email_login,
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        content=password_login,
                        padding=ft.padding.only(20, 10),
                    ),
                    ft.Container(
                        content=ft.Checkbox(
                            width=280,
                            height=40,
                            label='Recordar Contraseña',
                            check_color='black',
                        ),
                        padding=ft.padding.only(40),
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Text(
                                "INICIAR",
                                color='white',
                                weight='w500',
                            ),
                            width=280,
                            bgcolor='blue',
                            on_click=iniciar_sesion
                        ),
                        padding=ft.padding.only(25, 10),
                    ),
                    ft.Text('Iniciar sesión con',
                            text_align="CENTER",
                            width=120),
                    ft.Row([
                        ft.IconButton(
                            icon=ft.icons.EMAIL,
                            tooltip="Google",
                            icon_size=35,
                        ),
                        ft.IconButton(
                            icon=ft.icons.FACEBOOK,
                            tooltip="Facebook",
                            icon_size=35,

                        ),
                        ft.IconButton(
                            icon=ft.icons.APPLE,
                            tooltip="Apple",
                            icon_size=35,
                        ),
                        ft.IconButton(
                            icon=ft.icons.QR_CODE,
                            tooltip="qr",
                            icon_size=35,
                        )
                    ],
                        alignment=ft.MainAxisAlignment.CENTER),

                    ft.Container(
                        content=ft.Row([
                            ft.Text(
                                'No tienes cuenta?'
                            ),
                            ft.TextButton(
                                'Crear una cuenta',
                                on_click=animate
                            ),
                        ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=8),
                        padding=ft.padding.only(40)
                    ),
                ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),

                expand=True,
            ),

        ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        alignment=ft.alignment.center,
        width=450,
        height=700,
        gradient=ft.LinearGradient([
            ft.colors.BLUE_GREY_400,
            ft.colors.WHITE70,
            ft.colors.WHITE70,
            ft.colors.BLUE_GREY_400,
        ]),
        border_radius=40

    )

    c2 = ft.Container(
        content=ft.Row([

            ft.Container(
                content=ft.Column([
                    ft.Text(
                        'Crear Cuenta',
                        width=360,
                        size=30,
                        weight='w900',
                        text_align='center',
                        color="blue"
                    ),
                    ft.Row([
                        ft.Container(
                        content=name_register,
                       
                    ),
                    ft.Container(
                        content=apellido_register,
                        
                    ),],alignment=ft.MainAxisAlignment.CENTER),
                    
                    

                    ft.Container(
                        content=email_register,
                        padding=ft.padding.only(20, 10)
                    ),
                    ft.Container(
                        content=password_register,
                        padding=ft.padding.only(20, 10),
                    ),
                    ft.Container(
                        content=country_dropdown,
                        padding=ft.padding.only(20, 10),
                    ),
                    ft.Container(
                        content=thad_dropdown,
                        padding=ft.padding.only(20, 10),
                    ),
                    ft.Container(
                        content=Genero_dropdown,
                        padding=ft.padding.only(20, 10),
                    ),
                    

                    
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Text(
                                'Seleccionar Fecha de Nacimiento',
                                color='white',
                                weight='w500',
                            ),
                            width=280,
                            bgcolor='black',
                            on_click=lambda _: date_input.pick_date()
                        ),
                        padding=ft.padding.only(25, 10),
                    ),
                    
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Text(
                                'REGISTRARSE',
                                color='white',
                                weight='w500',
                              
                            ),
                            width=280,
                            bgcolor='blue',
                            on_click=registrarse
                        ),
                        padding=ft.padding.only(25, 10),
                    ),
                    ft.Container(
                        content=ft.Row([
                            ft.Text(
                                'Ya tienes una cuenta?'
                            ),
                            ft.TextButton(
                                'Iniciar sesion',
                                on_click=animate
                            ),
                        ], alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10),
                        padding=ft.padding.only(40)
                    ),
                ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                expand=True,
            ),
        ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        alignment=ft.alignment.center,
        width=450,
        height=700,
        gradient=ft.LinearGradient([
            ft.colors.BLUE_GREY_400,
            ft.colors.WHITE70,
            ft.colors.WHITE70,
            ft.colors.BLUE_GREY_400,
        ]),
        border_radius=40
    )
    

    c3 = ft.Container(
        width=450,
        gradient=ft.LinearGradient([
            ft.colors.WHITE,
        ]),

        
        border_radius= 40,

        content=ft.Row([
            ft.Container(
            
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15
            ),
            margin=ft.margin.only(
                top=page.window_height -90,
                left=0,
                right=10
            ),
            

            
            
            border_radius=30,
            width=page.window_width,
            bgcolor='blue',
            content=t
        )
        
            
                    

        ]),
        

         )
        
            

       
    

    
    listnavico = ft.Container(
        shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15
            ),
            
            
        )
    page.overlay.append(ft.Stack([
            ft.ResponsiveRow([
                ft.Column(col=12, controls=[
                    listnavico
                ])
            ]),

        ])

        )

    c = ft.AnimatedSwitcher(
        content=c1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.EASE,
    )
    page.add(c)

ft.app(target=main)
