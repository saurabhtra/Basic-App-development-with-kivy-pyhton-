from kivymd.app import MDApp
from kivy.lang import Builder

# to adjust the size of the window manually use the following two lines
#     from kivy.core.window import Window
#     Window.size =(300,500)

screen_helper = """
Screen:
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'Demo Application'
            left_action_items:[["menu",lambda x: app.navigation_draw()]]
            right_action_items:[["clock",lambda x: app.navigation_draw()]]
            elevation:8
        MDLabel:
            text:'THIS IS HACKER'
            halign:'center'
        MDBottomAppBar:
            MDToolbar:
                title:'Help Desk'
                left_action_items:[["settings",lambda x: app.navigation_draw()]]
                elevation:8
                mode:'end'
                type:'bottom'
                icon:'google'
                on_action_button:app.navigation_draw()
                
            
    

"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette ="Red"
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("good")

DemoApp().run()
