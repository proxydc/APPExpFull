from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.app import App
import psycopg2

class ExpGrid(Widget):
    shopname=ObjectProperty(None)
    shopby=ObjectProperty(None)
    foodtype=ObjectProperty(None)
    card=ObjectProperty(None)
    amount=ObjectProperty(None)
    wordlabel=ObjectProperty(None)
    def press(self):
        shopname=self.shopname.text
        shopby=self.shopby.text
        foodtype=self.foodtype.text
        card=self.card.text
        amount=self.amount.text
        wordlabel=self.wordlabel.text
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
        self.wordlabel.text = f'Your expense in {shopname} is added!'
        
        # Clear the input box
        #self.word_input.text =""
        
        # commit our changes
        conn.commit()
        
        #Close our connection
        conn.close()


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
            word = f'{word}\n{record[0]}'
            self.wordlabel.text = f'{word}'
        
        # commit our changes
        conn.commit()
        
        #Close our connection
        conn.close()
        
class ExpApp(App):
    def build(self):
        return ExpGrid()
    
if __name__ == "__main__":
    ExpApp().run()