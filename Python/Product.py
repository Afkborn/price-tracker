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

        self.__id = id # id
        self.__productName = productName # ürün ismi
        self.__productURL = productURL # ürün urlsi
        self.__productTime = productTime   # oluşturulma zamanı
        self.__checkStock = checkStock  # stok durumunun takip edilip edilmemesi
        self.__checkPrice = checkPrice # fiyat durumunun takip edilip edilmemesi
        self.__checkTime = checkTime # kontrol süresi 
        self.__price = price #fiyat bilgisi
        self.__stock = stock #stock bilgisi
        self.__priceTime = priceTime #fiyata ait olan zaman bilgisi
        self.__stockTime = stockTime #stoğa ait olan zaman bilgisi

    def __str__(self) -> str:
        return str((self.__id,self.__productName,self.__productURL,self.__productTime,self.__checkStock,self.__checkPrice,self.__checkTime,self.__price,self.__priceTime,self.__stock,self.__stockTime))

    def getId(self) -> int:
        """Return ID as int"""
        return self.__id
    def setId(self,id:int):
        """Set ID (int)"""
        self.__id = id

    def getProductName(self) -> str:
        """Return product name as string"""
        return self.__productName
    def setProductName(self,productName:str):
        """Set product name (str)"""
        self.__productName = productName

    def getProductURL(self)->str:
        """Return product URL as str"""
        return self.__productURL
    def setProductURL(self,productURL:str):
        """Set product URL (str)"""
        self.__productURL = productURL

    def getProductTime(self) -> int:
        """Return product time as int"""
        return self.__productTime
    def setProductTime(self,productTime:int):
        """Set product time(int)"""
        self.__productTime=productTime
    
    def getCheckStock(self) -> bool:
        """Return check stock as bool"""
        return self.__checkStock
    def setCheckStock(self,checkStock:bool):
        """Set check stock (bool)"""
        self.__checkStock = checkStock
    
    def getCheckPrice(self) -> bool:
        """Return check price as bool"""
        return self.__checkPrice
    def setCheckPrice(self,checkPrice:bool):
        """Set check price(bool)"""
        self.__checkPrice = checkPrice
    
    def getCheckTime(self) ->int:
        """Return check time as int"""
        return self.__checkTime
    def setCheckTime(self,checkTime:int):
        """Set check time (int)"""
        self.__checkTime = checkTime

    def getPrice(self) -> float:
        """Return price as float"""
        return self.__price
    def setPrice(self,price:int):
        """Set price (int)"""
        self.__price = price
    
    def getStock(self) -> bool:
        """Return stock as bool"""
        return self.__stock
    def setStock(self,stock:bool):
        """Set stock (bool)"""
        self.__stock = stock
    
    def getPriceTime(self) -> int:
        """Return price time as int"""
        return self.__priceTime
    def setPriceTime(self,priceTime:int):
        """Set price time(int)"""
        self.__priceTime = priceTime
    
    def getStockTime(self) ->int:
        """Return stock time as int"""
        return self.__stockTime
    def setStockTime(self,stockTime:int):
        """Set stock time (int)"""
        self.__stockTime = stockTime
        