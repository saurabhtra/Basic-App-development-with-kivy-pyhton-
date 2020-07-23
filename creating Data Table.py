from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(size_hint=(0.9, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            check=True,
                            rows_num=10,
                            column_data=[

                                ("No.", dp(30)),
                                ("Food", dp(30)),
                                ("Calories", dp(30))
                            ],
                            row_data=[
                                ("1","Burger", "300"),
                                ("2", "Burger", "300"),
                                ("3","Meggie", "400"),
                                ("4", "Meggie", "400"),
                                ("5", "Meggie", "400"),
                                ("6", "Meggie", "400"),
                                ("7", "Meggie", "400"),
                                ("8", "Meggie", "400"),
                                ("9", "Meggie", "400"),
                                ("10", "Meggie", "400")
                            ]
                            )
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)
        screen.add_widget(table)
        return screen
    def check_press(self,instance_table,current_row):
        print(instance_table,current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)


DemoApp().run()
