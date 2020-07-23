screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name:'menu'
    MDRectangleFlatButton:
        text:'Profile'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:root.manager.current ='profile'
    MDRectangleFlatButton:
        text:'Upload'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.manager.current ='upload'
<ProfileScreen>:
    name:'profile'
    MDLabel:
        text:'ThiS iS HackER'
        halign:'center'
    MDRectangleFlatButton:
        text:'BAck'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        on_press:root.manager.current ='upload'
<UploadScreen>:
    name:'upload'
    MDLabel:
        text:'Lets upload something'
        halign:'center'
    MDRectangleFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        on_press:root.manager.current ='menu'




"""