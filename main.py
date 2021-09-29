
from os import startfile, system,getcwd
from Python.Product import Product
from Python.Tracker import PriceTracker

from pyfiglet import Figlet
from pyfiglet import FigletFont
from colorama import Fore, Style
from msvcrt import getch
from time import time

MENUOPT = ["Check the prices of the product list","Add product to product list","Exit", "List product with id","Delete product with id","Add price manually with id","Get last price with id","Add stock manually with id","Get last stock state with id"]

def printPriceTracker():
    f = Figlet(font="chunky")
    print(Fore.CYAN)
    print(f.renderText(f'      Price\nTracker'))
    print(Style.RESET_ALL)





if __name__ == "__main__":
    detailText = []
    priceTracker = PriceTracker()
    detailText.append(f"{priceTracker.getDbLen()} adet kayıt başarıyla yüklendi.")
    menuControl = True
    selectedMenuOpt = 0
    selectedMenuSymbol = 'x'
    pressSpecialKey = False
    while menuControl:
        system('cls')
        printPriceTracker()

        if not pressSpecialKey:
            for index,i in enumerate(MENUOPT):
                if index == selectedMenuOpt:
                    print(f"[{selectedMenuSymbol}] {i}")
                else:
                    print(f"[ ] {i}")


                 
            for i in detailText:
                print(i)


        returnKey = getch()
        if returnKey == b'\x03': # Control + C
            menuControl = False
        elif returnKey == b'\xe0': # Special Key
            pressSpecialKey = True
        elif returnKey == b'H': # Up Arrow or H
            if pressSpecialKey: # Up Arrow
                if selectedMenuOpt == 0:
                    selectedMenuOpt = len(MENUOPT) - 1
                else:
                    selectedMenuOpt -= 1
                pressSpecialKey = False
        elif returnKey == b'P': # Down Arrow or P
            if pressSpecialKey: # Down Arrow
                if selectedMenuOpt == len(MENUOPT) -1:
                    selectedMenuOpt = 0
                else:
                    selectedMenuOpt +=1
                pressSpecialKey = False
        elif returnKey == b'\r':

            if selectedMenuOpt == 2:
                exit()
            elif selectedMenuOpt == 6:
                id = int(input("id"))
                myProduct  = priceTracker.getProductFromDbWithId(id)
                if myProduct == None:
                    detailText.append(f"No product found with id {id}")
                else:
                    detailText.append(f"ID: {myProduct.getId()} Price: {priceTracker.getLastPriceWithProductFromDb(myProduct)}")

            elif selectedMenuOpt == 7:
                id = int(input("id"))
                myProduct  = priceTracker.getProductFromDbWithId(id)
                if myProduct == None:
                    detailText.append(f"No product found with id {id}")
                else:
                    yn = input('Is the product in stock now? (y/n)').strip()
                    if "y" in yn or "Y" in yn:
                        priceTracker.addStockToDb(myProduct,True)
                    else:
                        priceTracker.addStockToDb(myProduct,False)
            elif selectedMenuOpt == 8:
                id = int(input("id"))
                myProduct  = priceTracker.getProductFromDbWithId(id)
                if myProduct == None:
                    detailText.append(f"No product found with id {id}")
                else:
                    detailText.append(f"ID: {myProduct.getId()} Stock: {priceTracker.getLastStockStateWithProductFromDb(myProduct)}")

            elif selectedMenuOpt == 5:
                id = int(input("id"))
                myProduct  = priceTracker.getProductFromDbWithId(id)
                if myProduct == None:
                    detailText.append(f"No product found with id {id}")
                else:
                    print(myProduct)
                    price = int(input("Price: "))
                    priceTracker.addPriceToDb(myProduct,price)
                    detailText.append(myProduct)
                

            elif selectedMenuOpt == 3:
                id = int(input("id"))
                myProduct  = priceTracker.getProductFromDbWithId(id)
                if myProduct == None:
                    detailText.append(f"No product found with id {id}")
                else:
                    detailText.append(myProduct)

            elif selectedMenuOpt == 4:
                id = int(input("id"))
                myProduct  = priceTracker.getProductFromDbWithId(id)
                if myProduct == None:
                    detailText.append(f"No product found with id {id}")
                else:
                    print(myProduct)
                    yn = input('Are you sure you want to delete? (y/n)').strip()
                    if "y" in yn or "Y" in yn:
                        
                        detailText.append(f"deletion successful with id {myProduct.getId()}")
                        priceTracker.deleteProduct(myProduct)
                    else:
                        detailText.append("Deletion canceled")

            elif selectedMenuOpt == 1:
                productURL = input("Product URL: ").strip()
                #TODO ürünün URL bilgisinden hangi e-ticaret sitesinde olduğunu kontrol et
                productURL = "htpps://www.fortesting.com/4541564654/41564654/564654654" # for testing
                
                productName = input("Product name: ").strip()
                productName = "for testing "

                priceTrack = input("Would you like to follow the price information of the product? (y/n)").strip()
                if "y" in priceTrack or "Y" in priceTrack:
                    checkPrice = True
                else:
                    checkPrice = False
                    
                stockTrack = input("Would you like to follow the stock information of the product? (y/n)").strip()
                if "y" in stockTrack or "Y" in stockTrack:
                    checkStock = True
                else:
                    checkStock = False
                productTime = time()

                try:
                    checkTime = input("How often would you like to be checked? (HH:MM:SS)(Ex: 00:10:00 every 10minute.) : ")
                    hour,minute,second = checkTime.split(":")
                    totalSec = (int(hour)*3600) + (int(minute)*60) + int(second)
                except:
                    totalSec = 600
                    print("Error! Default value 10 minute. You can change it in the product settings.")

                product = Product(productName=productName,productURL=productURL,productTime=productTime,checkStock=checkStock,checkPrice=checkPrice,checkTime=totalSec)
                productID = priceTracker.addProduct(product=product)
                product.setId(productID)
                detailText.append(f"The product named '{product.getProductName()}' has been added with the id number {product.getId()}.")




