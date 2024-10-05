from flet import*

def main(page:Page):
    page.window_width=450
    page.window_height=700
    page.bgcolor = colors.WHITE
    page.scroll="always"
    
    

    myicons=[
    "home","create","person","settings","favorite","grade","shopping_cart_checkout","expand_circle_down"]

    def youchange(e):
        pass
    t= Tabs(
        selected_index=0,
        animation_duration=100,
        indicator_color="white",
        divider_color="blue",
        scrollable=True,
        on_change= youchange,
        tabs=[]
    )

    for x in  myicons:
        t.tabs.append(
            Tab(
                tab_content=Icon(
                    name=x,
                    size=40,
                    color="white",
                )
            )  
        )
    mylist = Container(
        Row([
            Container(
                margin=margin.only(
            top=page.window_height/2
        ),
        content=Column([
            Icon(name="home",size=50),
            Text("home Screen",size=30)
        ], spacing=8),
           expand=True,
           padding=padding.only(20,10)
            )
        ])

        
    ) 
    
    listnavico= Container(
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=15
        ),
        margin=margin.only(
            top=page.window_height-100,
            left=10,
            right=10
        ),
        border_radius=30,
        width=page.window_width,
        bgcolor='blue',
        content=t
    )

    def youtaphere (e):
        page.di=AlertDialog(
            title= Text("Open you dialog",size=30),
            content=Text("this sample"),
            actions=[
                ElevatedButton("Close"),
                ElevatedButton("test")
            ],
        
        )
    
    page.overlay.append(Stack([
        ResponsiveRow([
            Column(col=12,controls=[
                listnavico
            ])
        ]),
        Container(
            padding=10,
            margin= margin.only(
                top=page.window_height-150,
                left=page.window_width/2-35,
                right=page.window_width/2-35,
            ),
        bgcolor="blue",
        border=border.all(5,"white"),
        shape=BoxShape.CIRCLE,
        content=GestureDetector(
            mouse_cursor=MouseCursor.CLICK,
            on_tap=youtaphere,
            content=Icon(name="add",size=28,color="white")

        )

        )
    ])
    
    )

    page.add(
        Row([
            mylist
        ],alignment="center")
        
        )
    
    
app(target=main)


