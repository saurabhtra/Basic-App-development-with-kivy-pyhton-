from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
# there is no need to import MDTextField over here as it will be loaded
# by BUilder
# from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from helper import username_helper


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"
        # username=MDTextField(text='enter user name',pos_hint=
        # {'center_x':0.5,'center_y':0.5},
        #                   size_hint_x=None,width=300)
        self.username = Builder.load_string(username_helper)
        btn = MDRectangleFlatButton(text="show", pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                    on_release=self.show_data)

        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text +'                    does not exists'
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')

        self.dialog = MDDialog(title='username check', text=check_string
                               , size_hint=(0.7, 1),
                               buttons=[close_button, more_button])
        self.dialog.open(())

    def close_dialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()
