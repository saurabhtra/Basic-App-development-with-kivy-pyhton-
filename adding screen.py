from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton

class DemoApp(MDApp):


    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue="900"
        self.theme_cls.theme_style="Dark"
        btn_flat=MDRectangleFlatButton(text="this is hacker",
                              pos_hint={'center_x':0.5,
                                        'center_y':0.5})
        icon_btn=MDFloatingActionButton(icon='android',pos_hint={'center_x':0.4,'center_y':0.5})
        screen.add_widget(btn_flat)
        screen.add_widget(icon_btn)
        return screen





DemoApp().run()
