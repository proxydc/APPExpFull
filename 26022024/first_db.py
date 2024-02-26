from kivy.lang import Builder
from kivymd.app import MDApp
import psycopg2

class MainAPp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        #return Builder.load_file('first_db.kv')
    
        # Define DB stuff
        conn = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "Proxiad2024*!",            
            port = "5432",
        )
        
        # Create A Cursor
        c = conn.cursor()
        
        # Create A Table
        c.execute("""CREATE TABLE if not exists expenses
            (name TEXT);
            """)
        
        # Check to see if table created
        #c.execute("SELECT * FROM customers")
        #print(c.description)
        
        # Commit our changes
        conn.commit()
        
        # Close our connection
        conn.close()
        
        return Builder.load_file('first_db.kv')
    
    def submit(self):
        shopname=self.root.ids.shopname.text
        shopby=self.root.ids.shopby.text
        foodtype=self.root.ids.foodtype.text
        card=self.root.ids.card.text
        amount=self.root.ids.amount.text
        wordlabel=self.root.ids.wordlabel.text
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
        self.root.ids.wordlabel.text = f'Your expense in {shopname} is added!'
        
        # Clear the input box
        #self.root.ids.word_label.text =""
        
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
            word = f'{word}{record[0]}\n'
            self.root.ids.wordlabel.text = f'{word}'
        
        # commit our changes
        conn.commit()
        
        #Close our connection
        conn.close()
        
MainAPp().run()