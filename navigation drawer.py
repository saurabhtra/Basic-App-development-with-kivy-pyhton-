from kivymd.app import MDApp
from kivy.lang import Builder

navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title:'Demo Application'
                        
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]                       
                        elevation:10
                    Widget:
        MDNavigationDrawer:
            id:nav_drawer
            BoxLayout:                
                orientation:'vertical'  
                spacing:'10dp'
                padding:'10dp'
                Image:
                    source: 'pic.jpg'                  
                MDLabel:
                    text:'Saurabh Gangwar'
                    font_style:'Subtitle1'
                    size_hint_y:None
                    height:self.texture_size[1]
                MDLabel:                    
                    text:'saurabhgangwar@gmail.com'   
                    font_style:'Caption'
                    size_hint_y:None
                    height:self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            IconLeftWidget:
                                icon:'face-profile-woman'
                        OneLineIconListItem:
                            text:'Upload'   
                            IconLeftWidget:
                                icon:'file-upload'
                        OneLineIconListItem:
                            text:'Logout'   
                            IconLeftWidget:
                                icon:'logout'
                        
                        
            
            
                    
"""
class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen
DemoApp().run()