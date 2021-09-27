from os import getcwd
from os.path import exists
import sqlite3 as sql

CREATETABLEPRODUCT = """CREATE TABLE products (id	INTEGER PRIMARY KEY,productName varchar(20) NOT NULL,productURL varchar(20) NOT NULL,productTime INTEGER NOT NULL)"""

class PriceTracker:
    isLoadDB = False
    dbName = "database.db"
    dbLoc = f"{getcwd()}\Database\{dbName}"
    def __init__(self) -> None:
        self.__checkDB()

    def __loadDB(self):
        try:
            self.db = sql.connect(self.dbLoc)
            self.im = self.db.cursor()
            self.im.execute("SELECT name FROM sqlite_master")
            tableNames = self.im.fetchall()
            if "products" in tableNames[0]:
                self.im.execute("SELECT * FROM products")
                self.products = self.im.fetchall()
                self.isLoadDB = True
            else:
                self.im.execute(CREATETABLEPRODUCT)
                self.isLoadDB = True
        except:
            self.isLoadDB = False

    def __checkDB(self):
        if exists(self.dbLoc):
            self.__loadDB()
        else:
            self.db = sql.connect(self.dbLoc)
            self.im = self.db.cursor()
            self.im.execute(CREATETABLEPRODUCT)
            self.isLoadDB = True
    
    
# self.im.execute("INSERT INTO products(productName,productURL,productTime) VALUES('rx590','deneme',15)")


if __name__ == "__main__":
    pass