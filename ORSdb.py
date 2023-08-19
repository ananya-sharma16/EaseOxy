import sqlite3

def create_conn():

    global conn
    global cursr
    conn = sqlite3.connect('ORS_database.db')
    cursr = conn.cursor()

    conn.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER
                (NAME TEXT PRIMARY KEY,
                CYLINDERS INT,
                SHOP TEXT,
                RENTAL_BASIS INT,
                RENTAL_TIME TEXT,
                BILL REAL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS RENTAL
                (NAME TEXT PRIMARY KEY,
                STOCK_TOTAL INT,
                STOCK INT);''')

def insert_customer(name):
    conn.execute("INSERT INTO CUSTOMER (NAME) VALUES (?)", (name,))

def insert_shop(name, t_stock, stock):
    conn.execute("INSERT INTO RENTAL VALUES (?, ?, ?)", (name, t_stock, stock))

def increase_stock(name, nos):
    conn.execute("UPDATE RENTAL SET STOCK_TOTAL = STOCK_TOTAL + (?), STOCK = STOCK + (?) WHERE NAME = (?)", (nos, nos, name))

def decrease_stock(name, nos):
    conn.execute("UPDATE RENTAL SET STOCK_TOTAL = STOCK_TOTAL - (?), STOCK = STOCK - (?) WHERE NAME = (?)", (nos, nos, name))

def update_rent(name, cylinder, shop, basis, time):
    conn.execute("UPDATE CUSTOMER SET CYLINDERS = (?), SHOP = (?), RENTAL_BASIS = (?), RENTAL_TIME = (?) WHERE NAME = (?)", (cylinder, shop, basis, time, name))
    conn.execute("UPDATE RENTAL SET STOCK = STOCK - (?) WHERE NAME = (?)", (cylinder, shop))

def update_return(name, shop, cylinder):
    conn.execute("UPDATE CUSTOMER SET CYLINDERS = NULL, SHOP = NULL, RENTAL_BASIS = NULL, RENTAL_TIME = NULL WHERE NAME = (?)", (name,))
    conn.execute("UPDATE RENTAL SET STOCK = STOCK + (?) WHERE NAME = (?)", (cylinder, shop))

def display_tables():
    print("Customer Table:")
    for x in conn.execute("SELECT * FROM CUSTOMER"):
        print(x)

    print("Rental Table:")
    for x in conn.execute("SELECT * FROM RENTAL"):
        print(x)

    print("\n")


'''update_rent('Parth', 2, 'Air_Rentals', 3, '2021-11-23 09:34:23.654783')

conn.execute("INSERT INTO CUSTOMER VALUES ('Kent', 3, 'Pure_Rentals', 2, '2021-11-22 09:06:54.675432', 0)")

update_return('John', 'Blue_Rentals', 5)'''

create_conn()
display_tables()


