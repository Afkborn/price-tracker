from os import getcwd
from os.path import exists
import sqlite3 as sql
from Python.Product import Product
from time import time

CREATETABLEPRODUCT = """CREATE TABLE IF NOT EXISTS products (id	INTEGER PRIMARY KEY,productName TEXT NOT NULL,productURL TEXT NOT NULL,productTime INTEGER NOT NULL,checkStock TEXT NOT NULL, checkPrice TEXT NOT NULL,checkTime INTEGER NOT NULL)"""
CREATETABLEPRICES = """CREATE TABLE IF NOT EXISTS prices (id INTEGER NOT NULL, priceTime INTEGER NOT NULL, price INTEGER NOT NULL)"""
CREATETABLESTOCKS = """CREATE TABLE IF NOT EXISTS stocks (id INTEGER NOT NULL, stockTime INTEGER NOT NULL, stock TEXT NOT NULL)"""

class PriceTracker:

    __isLoadDB = False
    __dbName = "database.db"
    __products = []
    __dbLen = 0
    __dbLoc = f"{getcwd()}\Database\{__dbName}"

    def __init__(self) -> None:
        self.checkDB()

    def getDbName(self) -> str:
        """Database adını döner"""
        return self.__dbName
    def getIsLoadDb(self) -> bool:
        """Database'in yüklenip yüklenmediğini döner"""
        return self.__isLoadDB
    def getDbLen(self):
        """Databasede kayıtlı olan productların uzunluğunu döner"""
        self.checkDB()
        return self.__dbLen
    def getProductsList(self) -> list:
        """Product listesini döner"""
        self.checkDB()
        return self.__products
    def getDbLoc(self) -> str:
        return self.__dbLoc


    def checkDB(self):
        """Database dosyasını kontrol eder, eğer konumda database dosyası varsa yüklemeye yarayan loadDb fonksiyonu çalışır yoksa o konumda bir database dosyası oluşturmaya yarayan createDb çalışır"""
        if exists(self.__dbLoc):
            #Konumda varsa
            self.__loadDB()
        else:
            #Konumda yoksa
            self.__createDB

    def __loadDB(self):
        """Database dosyasını yüklemeye yarar. Yüklenen değerler Product Classından bir obje olarak products listesine eklenir. """
        self.__products = []
        self.db = sql.connect(self.__dbLoc)
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
                if checkStock == "True":
                    checkStock = True
                else:
                    checkStock = False
                if checkPrice == "True":
                    checkPrice = True
                else:
                    checkPrice = False
                findProduct = Product(id,productName,productURL,productTime,checkStock,checkPrice,checkTime)
                if checkPrice:
                    self.getLastPriceWithProductFromDb(findProduct)
                if checkStock:
                    self.getLastStockStateWithProductFromDb(findProduct)
                self.__products.append(findProduct)
            self.__isLoadDB = True
        else:
            self.im.execute(CREATETABLEPRODUCT)
            self.im.execute(CREATETABLEPRICES)
            self.im.execute(CREATETABLESTOCKS)
            self.__isLoadDB = True
        self.db.close()
        self.getProductLenFromDB()

    def __createDB(self):
        """kayıtlı konumda (öğrenmek için getDbLoc fonksiyonu kullanılabilir) database oluşturur. """
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(CREATETABLEPRODUCT)
        self.im.execute(CREATETABLEPRICES)
        self.im.execute(CREATETABLESTOCKS)
        self.__isLoadDB = True
        self.db.close()
        self.__dbLen = 0


    def addProduct(self,product:Product) ->int:
        """Database'e ürün ekler ve son eklenen ürünün id bilgisini döner."""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"INSERT INTO products(productName,productURL,productTime,checkStock,checkPrice,checkTime) VALUES('{product.getProductName()}','{product.getProductURL()}',{product.getProductTime()},'{product.getCheckStock()}','{product.getCheckPrice()}',{product.getCheckTime()})")
        self.db.commit()
        self.db.close()
        lastInsertID = self.getProductFromDbWithProductTime(product.getProductTime()).getId()
        return lastInsertID
    
    def addPriceToDb(self,product:Product, price : float):
        """Database üzerinde bulunan Prices tablosuna verilen Product objesi için fiyat bilgisi ekler. """
        product.setPrice(price)
        product.setPriceTime(time())
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"INSERT INTO prices(id,priceTime,price) VALUES('{product.getId()}','{product.getPriceTime()}','{product.getPrice()}')")
        self.db.commit()
        self.db.close()
    
    def addStockToDb(self,product:Product, stock : bool):
        """Database üzerinde bulunan Stocks tablosuna verilen Product objesi için stok bilgisi ekler. """
        product.setStock(stock)
        product.setStockTime(time())
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"INSERT INTO stocks(id,stockTime,stock) VALUES('{product.getId()}','{product.getStockTime()}','{product.getStock()}')")
        self.db.commit()
        self.db.close()

    def deleteProduct(self,product:Product) -> bool:
        """Ürün Siler"""
        productId = product.getId()
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"DELETE FROM products WHERE id = '{productId}'")
        #TODO ürüne ait olan stock ve price bilgilerinide sil.
        self.db.commit()
        self.db.close()
    
    def getProductFromDbWithId(self,id) -> Product:
        """ID si verilen product objesini database'de arar varsa onu döner yoksa none döner."""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM products WHERE id = '{id}'")
        findProduct = self.im.fetchone()
        if findProduct == None:
            return None
        id, productName, productURL, productTime, checkStock, checkPrice, checkTime = findProduct
        
        if checkStock == "True":
            checkStock = True
        else:
            checkStock = False
        
        if checkPrice == "True":
            checkPrice = True
        else:
            checkPrice = False

        findProduct = Product(id,productName,productURL,productTime,checkStock,checkPrice,checkTime)
        if checkPrice:
            self.getLastPriceWithProductFromDb(findProduct)
        if checkStock:
            self.getLastStockStateWithProductFromDb(findProduct)
        self.db.close()
        return findProduct
    
    def getLastPriceWithProductFromDb(self, product:Product)-> float:
        """verilen Product objesine ait son fiyat bilgisini databaseden sorgu yaparak float cinsinde döner."""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(F"SELECT MAX(priceTime),price FROM prices WHERE id = '{product.getId()}'")
        priceTime, price = self.im.fetchone()
        if priceTime == None and price == None:
            return None
        product.setPriceTime(priceTime)
        product.setPrice(price)
        return product.getPrice()
    

    def getLastStockStateWithProductFromDb(self,product:Product) -> bool:
        """verilen product objesine ait son stok bilgisini databaseden sorgu yaparak bool cinsinden döner."""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(F"SELECT MAX(stockTime),stock FROM stocks WHERE id = '{product.getId()}'")
        stockTime, stock = self.im.fetchone()
        if stockTime == None and stock == None:
            return None
        if stock == "True":
            stock = True
        else:
            stock = False
        product.setStockTime(stockTime)
        product.setStock(stock)
        return product.getStock()


    def getProductFromDbWithProductTime(self,productTime):
        """Product sınıfından oluşturulan objenin oluştuğu süreye göre arama yapıp bulunan ürünü döner, yoksa None döner."""
        """ if find return Product or none"""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM products WHERE productTime = '{productTime}'")
        findProduct = self.im.fetchone()
        if findProduct == None:
            return None
        id, productName, productURL, productTime, checkStock, checkPrice, checkTime = findProduct
        findProduct = Product(id,productName,productURL,productTime,checkStock,checkPrice,checkTime)
        self.db.close()
        return findProduct 

    def getProductLenFromDB(self) -> int:
        """Database'de kayıtlı olan products listesinin uzunluğunu döner."""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute("select last_insert_rowid() from products")
        self.__dbLen = len(self.im.fetchall())
        self.db.close() 
        return self.__dbLen 

    def getIdListFromDb(self) -> list:
        """Database'e gidip products tablosundaki ürünlerin ID bilgisini döner."""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute("select id from products")
        idListe = []
        idList = self.im.fetchall()
        for i in idList:
            idListe.append(i[0])
        return idListe


    

if __name__ == "__main__":
    pass