from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import psycopg2
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

Window.clearcolor = 0, 1, 1, 1,
# Define our different screens
class FirstWindow(Screen):
    wordlabel=StringProperty("Details Here")
    shopname=ObjectProperty(None)
    shopby=ObjectProperty(None)
    foodtype=ObjectProperty(None)
    card=ObjectProperty(None)
    amount=ObjectProperty(None)    
    def submit(self):
        print(self.wordlabel)
        print(self.ids.shopname.text)
        self.wordlabel = "Success"
        shopname=self.ids.shopname.text
        shopby=self.ids.shopby.text
        foodtype=self.ids.foodtype.text
        card=self.ids.card.text
        amount=self.ids.amount.text
        #wordlabel=self.root.ids.wordlabel.text
        # Create Database or Connect To One
        conn = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "Proxiad2024*!",            
            port = "5432",
        )
        
        # Create A Cursor
        c = conn.cursor()
        
        # add A Record
        sql_command = "INSERT INTO expenses (shopname, shopby, foodtype, card, amount) VALUES(%s,%s,%s,%s,%s)"
        values = (shopname, shopby, foodtype, card, amount)
        
        # Execute SQL Command
        c.execute(sql_command, values)
        

        # Add a little message
        self.wordlabel = f'Your expense in {shopname} is added!'
        
        # Clear the input box
        #self.root.ids.word_label.text =""
        
        # commit our changes
        conn.commit()
        
        #Close our connection
        conn.close()

class SecondWindow(Screen):
    pass



class WindowManager(ScreenManager):
    pass

# Designate Our .kv design file
kv = Builder.load_file('new_window.kv')

class AwesomeApp(App):

    def build(self):
        return kv

 

    def show_records(self):
        # Create Database or Connect To One
        conn = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "Proxiad2024*!",            
            port = "5432",
        )
        #    conn = psycopg2.connect(
        #    host = "dpg-cn1pfl0l6cac73ffc1v0-a",
        #    database = "postgres1_8q91",
        #    user = "postgres1_8q91_user",
        #    password = "SlVRbeYlHb9OCqynKa0lTkON7U2H9cWs",            
        #    port = "5432",
        #)
        
        # Create A Cursor
        c = conn.cursor()
        
       
        # Grab records from database
        c.execute("SELECT * FROM expenses")
        records = c.fetchall()
        
        word = ''
        # Loop through records
        for record in records:
            word = f'{word}{record[0]}\n'
            self.root.ids.wordlabel2.text = f'{word}'
        
        # commit our changes
        conn.commit()
        
        #Close our connection
        conn.close()


if __name__ == '__main__':
    AwesomeApp().run()
