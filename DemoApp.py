from kivymd.app import MDApp
from kivymd.uix.label import  MDLabel,MDIcon


class DemoApp(MDApp):
    def build(self):
        label=MDLabel(text="THIS IS HACKER",halign='center',theme_text_color='Custom'
                      ,text_color=(  236/ 225.0,152/255.0,142/255.0,1)
                      ,font_style='H1')
        icon=MDIcon(icon="google",halign='center')
        return icon,label




DemoApp().run()