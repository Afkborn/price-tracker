from os import getcwd
from os.path import exists
import sqlite3 as sql
from Python.Product import Product
CREATETABLEPRODUCT = """CREATE TABLE products (id	INTEGER PRIMARY KEY,productName TEXT NOT NULL,productURL TEXT NOT NULL,productTime INTEGER NOT NULL,checkStock TEXT NOT NULL, checkPrice TEXT NOT NULL)"""

class PriceTracker:
    isLoadDB = False
    dbName = "database.db"
    products = []
    dbLen = 0
    dbLoc = f"{getcwd()}\Database\{dbName}"
    def __init__(self) -> None:
        self.__checkDB()


    def __loadDB(self):
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
        self.db.close()
        self.getProductLenFromDB()

    def __checkDB(self):
        if exists(self.dbLoc):
            self.__loadDB()
        else:
            self.db = sql.connect(self.dbLoc)
            self.im = self.db.cursor()
            self.im.execute(CREATETABLEPRODUCT)
            self.isLoadDB = True
            self.db.close()
            self.dbLen = 0

    def addProduct(self,product:Product) ->int:
        """Return last insert row id as int."""
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"INSERT INTO products(productName,productURL,productTime,checkStock,checkPrice) VALUES('{product.getProductName()}','{product.getProductURL()}',{product.getProductTime()},'{product.getCheckStock()}','{product.getCheckPrice()}')")
        self.db.commit()
        self.db.close()
        lastInsertID = self.getProductLenFromDB()
        return lastInsertID

    def getProductLenFromDB(self) -> int:
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute("select last_insert_rowid() from products")
        self.dbLen = len(self.im.fetchall())
        self.db.close() 
        return self.dbLen

    def getDbLen(self):
        return self.dbLen
    def getProducts(self):
        return self.products

    


    
# self.im.execute("INSERT INTO products(productName,productURL,productTime) VALUES('rx590','deneme',15)")


if __name__ == "__main__":
    pass