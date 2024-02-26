from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
#Display Pixles

class MyApp(MDApp):
    def build(self):
        # Define Screen
        screen = Screen()

        # Define Table
        table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.6),
            check = True,
            column_data = [
                ("Date", dp(30)),
                ("Shop", dp(30)),
                ("Shop-By", dp(30)),
                ("Amount", dp(30)),
                ("Card", dp(30)),
                ("TypeF", dp(30)),
            ],
            row_data = [
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),
                ("21/02/2024", "Lidl", "Alex", "25.25", "Hello", "Food"),



            ]
        )

        #bind the table
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)


        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        #return  Builder.load_file('table.kv')
        # add table widget to screen
        screen.add_widget(table)

        return screen
    # Function for check presses
    def checked(self, instance_table, current_row):
        print(instance_table, current_row)
    # Function for row presses
    def row_checked(self, instance_table, instance_row):
        print(instance_table, instance_row)
if __name__=="__main__":
    MyApp().run()