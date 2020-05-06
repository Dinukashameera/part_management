import pyodbc


class Databases:
    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server="SERVER NAME";'
                                   'Database=part_manager;'
                                   'Trusted_Connection=yes;')
        self.cur = self.conn.cursor()
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        row = self.cur.fetchall()
        return row

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES(?,?,?,?)",
                         (part, customer, retailer, price))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM parts WHERE partId = ?", (id))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, cutomer = ?,retailer = ?,price = ? WHERE partId = ?",
                     (part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



# db = Databases()
# db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
# db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
# db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")
