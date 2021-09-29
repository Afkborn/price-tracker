class Product:
    def __init__(
        self,id:int = None,
        productName:str = None,
        productURL:str = None,
        productTime:int = None,
        checkStock:bool = None,
        checkPrice:bool = None,
        checkTime:int = None,
        price:float = None,
        stock:bool = None,
        priceTime:int = None,
        stockTime:int = None) -> None:

        self.__id = id
        self.__productName = productName
        self.__productURL = productURL
        self.__productTime = productTime
        self.__checkStock = checkStock
        self.__checkPrice = checkPrice
        self.__checkTime = checkTime
        self.__price = price
        self.__stock = stock
        self.__priceTime = priceTime
        self.__stockTime = stockTime

    def __str__(self) -> str:
        return str((self.__id,self.__productName,self.__productURL,self.__productTime,self.__checkStock,self.__checkPrice,self.__checkTime,self.__price,self.__priceTime,self.__stock,self.__stockTime))

    def getId(self) -> int:
        return self.__id
    def setId(self,id:int):
        self.__id = id

    def getProductName(self) -> str:
        return self.__productName
    def setProductName(self,productName:str):
        self.__productName = productName

    def getProductURL(self)->str:
        return self.__productURL
    def setProductURL(self,productURL:str):
        self.__productURL = productURL

    def getProductTime(self) -> int:
        return self.__productTime
    def setProductTime(self,productTime:int):
        self.__productTime=productTime
    
    def getCheckStock(self) -> bool:
        return self.__checkStock
    def setCheckStock(self,checkStock:bool):
        self.__checkStock = checkStock
    
    def getCheckPrice(self) -> bool:
        return self.__checkPrice
    def setCheckPrice(self,checkPrice:bool):
        self.__checkPrice = checkPrice
    
    def getCheckTime(self) ->int:
        return self.__checkTime
    def setCheckTime(self,checkTime):
        self.__checkTime = checkTime

    def getPrice(self) -> float:
        return self.__price
    def setPrice(self,price):
        self.__price = price
    
    def getStock(self) -> bool:
        return self.__stock
    def setStock(self,stock:bool):
        self.__stock = stock
    
    def getPriceTime(self) -> int:
        return self.__priceTime
    def setPriceTime(self,priceTime:int):
        self.__priceTime = priceTime
    
    def getStockTime(self) ->int:
        return self.__stockTime
    def setStockTime(self,stockTime:int):
        self.__stockTime = stockTime
        