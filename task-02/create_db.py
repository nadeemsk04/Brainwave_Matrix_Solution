import sqlite3

def create_db():
    con = sqlite3.connect(database=r"inventory.db")
    c = con.cursor()

    try:
        # Create Users Table
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 dob TEXT NOT NULL,
                 email TEXT NOT NULL,
                 contact TEXT NOT NULL,
                 gender TEXT NOT NULL,
                 password TEXT NOT NULL,
                 type TEXT NOT NULL)''')

        # Create Product Table
        c.execute('''CREATE TABLE IF NOT EXISTS product (
                 product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 product_category TEXT NOT NULL,
                 product_name TEXT NOT NULL,
                 product_quantity INTEGER NOT NULL,
                 product_price REAL NOT NULL,
                 product_status TEXT NOT NULL)''')

        # Create Tracking Table with foreign key
        c.execute('''CREATE TABLE IF NOT EXISTS tracking (
                 tracking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 product_id INTEGER NOT NULL,
                 product_name TEXT NOT NULL,
                 quantity INTEGER NOT NULL, 
                 recorder_level INTEGER NOT NULL,
                 FOREIGN KEY (product_id) REFERENCES product(product_id)
                  )''')

        # Create Category Table 
        c.execute('''CREATE TABLE IF NOT EXISTS category (
                 category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 category_name TEXT NOT NULL
                  )''')


   
        con.commit()

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        con.close()  # Ensure the connection is closed

create_db()
