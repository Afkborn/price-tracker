class Product:
    def __init__(self,id:int = None,productName:str = None, productURL:str = None, productTime:int = None,checkStock:bool = None,checkPrice:bool = None) -> None:
        self.id = id
        self.productName = productName
        self.productURL = productURL
        self.productTime = productTime
        self.checkStock = checkStock
        self.checkPrice = checkPrice

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
        