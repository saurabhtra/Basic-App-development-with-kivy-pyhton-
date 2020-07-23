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
                        right_action_items:[["clock",lambda x:app.navigation_draw()]]
                        elevation:8
                    MDLabel:
                        text:'THIS IS HACKER'
                        font_size:100
                               
                    
                    
                        halign:'center'
                    Widget:
                    MDBottomAppBar:
                        MDToolbar:
                            title:'Help Desk'
                            left_action_items:[["settings",lambda x: app.navigation_draw()]]
                            elevation:8
                            mode:'end'
                            type:'bottom'
                            icon:'google'
                            on_action_button:app.navigation_draw()

        MDNavigationDrawer:
            id:nav_drawer
        



"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_string(navigation_helper)
        return screen

    def navigation_draw(self):
        print("well done")



DemoApp().run()
