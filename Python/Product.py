class Product:
    def __init__(self,id:int = None,productName:str = None, productURL:str = None, productTime:int = None,checkStock:bool = None,checkPrice:bool = None,checkTime:int = None,price:float = None, stock:bool = None) -> None:
        self.id = id
        self.productName = productName
        self.productURL = productURL
        self.productTime = productTime
        self.checkStock = checkStock
        self.checkPrice = checkPrice
        self.checkTime = checkTime
        self.price = price
        self.stock = stock

    def getId(self) -> int:
        return self.id
    def setId(self,id:int):
        self.id = id

    def getProductName(self) -> str:
        return self.productName
    def setProductName(self,productName:str):
        self.productName = productName

    def getProductURL(self)->str:
        return self.productURL
    def setProductURL(self,productURL:str):
        self.productURL = productURL

    def getProductTime(self) -> int:
        return self.productTime
    def setProductTime(self,productTime:int):
        self.productTime=productTime
    
    def getCheckStock(self) -> bool:
        return self.checkStock
    def setCheckStock(self,checkStock:bool):
        self.checkStock = checkStock
    
    def getCheckPrice(self) -> bool:
        return self.checkPrice
    def setCheckPrice(self,checkPrice:bool):
        self.checkPrice = checkPrice
    
    def getCheckTime(self) ->int:
        return self.checkTime
    def setCheckTime(self,checkTime):
        self.checkTime = checkTime

    def getPrice(self) -> float:
        return self.price
    def setPrice(self,price):
        self.price = price
    
    def getStock(self) -> bool:
        return self.stock
    def setStock(self,stock:bool):
        self.stock = stock
        