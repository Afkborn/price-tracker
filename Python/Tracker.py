from os import getcwd
from os.path import exists
import sqlite3 as sql
from Python.Product import Product
CREATETABLEPRODUCT = """CREATE TABLE IF NOT EXISTS products (id	INTEGER PRIMARY KEY,productName TEXT NOT NULL,productURL TEXT NOT NULL,productTime INTEGER NOT NULL,checkStock TEXT NOT NULL, checkPrice TEXT NOT NULL,checkTime INTEGER NOT NULL)"""
CREATETABLEPRICES = """CREATE TABLE IF NOT EXISTS prices (id INTEGER NOT NULL, productTime INTEGER NOT NULL, price INTEGER NOT NULL)"""
CREATETABLESTOCKS = """CREATE TABLE IF NOT EXISTS stocks (id INTEGER NOT NULL, productTime INTEGER NOT NULL, stock TEXT NOT NULL)"""
class PriceTracker:
    isLoadDB = False
    dbName = "database.db"
    products = []
    dbLen = 0
    dbLoc = f"{getcwd()}\Database\{dbName}"
    def __init__(self) -> None:
        self.checkDB()


    def __loadDB(self):
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute("SELECT name FROM sqlite_master")
        tableNames = self.im.fetchall()
        newTableNames = []
        for i in tableNames:
            i = str(i).replace("(","").replace(")","").replace("'","").replace(",","")
            newTableNames.append(i)
        tableNames = newTableNames
        if "products" in tableNames and "prices" in tableNames and "stocks" in tableNames:
            self.im.execute("SELECT * FROM products")
            allDb = self.im.fetchall()
            for i in allDb:
                id, productName, productURL, productTime, checkStock, checkPrice, checkTime = i
                newProduct = Product(id,productName,productURL,productTime,checkStock,checkPrice,checkTime)
                self.products.append(newProduct)
            self.isLoadDB = True
        else:
            self.im.execute(CREATETABLEPRODUCT)
            self.im.execute(CREATETABLEPRICES)
            self.im.execute(CREATETABLESTOCKS)
            self.isLoadDB = True
        self.db.close()
        self.getProductLenFromDB()

    def checkDB(self):
        if exists(self.dbLoc):
            self.__loadDB()
        else:
            self.db = sql.connect(self.dbLoc)
            self.im = self.db.cursor()
            self.im.execute(CREATETABLEPRODUCT)
            self.im.execute(CREATETABLEPRICES)
            self.im.execute(CREATETABLESTOCKS)
            self.isLoadDB = True
            self.db.close()
            self.dbLen = 0

    def addProduct(self,product:Product) ->int:
        """Return last insert row id as int."""
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"INSERT INTO products(productName,productURL,productTime,checkStock,checkPrice,checkTime) VALUES('{product.getProductName()}','{product.getProductURL()}',{product.getProductTime()},'{product.getCheckStock()}','{product.getCheckPrice()}',{product.getCheckTime()})")
        self.db.commit()
        self.db.close()
        lastInsertID = self.getProductFromDbWithProductTime(product.getProductTime()).getId()
        return lastInsertID

    def deleteProduct(self,product:Product) -> bool:
        productId = product.getId()
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"DELETE FROM products WHERE id = '{productId}'")
        self.db.commit()
        self.db.close()
    
    def getProductFromDbWithId(self,id) -> Product:
        """ if find return Product or none"""
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM products WHERE id = '{id}'")
        findProduct = self.im.fetchone()
        id, productName, productURL, productTime, checkStock, checkPrice, checkTime = findProduct
        findProduct = Product(id,productName,productURL,productTime,checkStock,checkPrice,checkTime)
        self.db.close()
        return findProduct
    
    def getProductFromDbWithProductTime(self,productTime):
        """ if find return Product or none"""
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM products WHERE productTime = '{productTime}'")
        findProduct = self.im.fetchone()
        id, productName, productURL, productTime, checkStock, checkPrice, checkTime = findProduct
        findProduct = Product(id,productName,productURL,productTime,checkStock,checkPrice,checkTime)
        self.db.close()
        return findProduct 
        
    def getProductLenFromDB(self) -> int:
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute("select last_insert_rowid() from products")
        self.dbLen = len(self.im.fetchall())
        self.db.close() 
        return self.dbLen

    def getDbLen(self):
        return self.dbLen

    def getProductsList(self) -> Product:
        self.checkDB()
        return self.products

    


    
# self.im.execute("INSERT INTO products(productName,productURL,productTime) VALUES('rx590','deneme',15)")


if __name__ == "__main__":
    pass