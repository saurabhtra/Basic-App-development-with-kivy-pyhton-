from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from screen_nav import screen_helper

class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class UploadScreen(Screen):
    pass

sn=ScreenManager()
sn.add_widget(MenuScreen(name='menu'))
sn.add_widget(ProfileScreen(name='profile'))
sn.add_widget(UploadScreen(name='upload'))
class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
DemoApp().run()