
from os import startfile, system,getcwd
from Python.Product import Product
from Python.Tracker import PriceTracker
from pyfiglet import Figlet
from pyfiglet import FigletFont
from colorama import Fore, Style
from msvcrt import getch
from time import time

MENUOPT = ["Check the prices of the product list","Add product to product list","Exit"]

def printPriceTracker():
    f = Figlet(font="chunky")
    print(Fore.CYAN)
    print(f.renderText(f'      Price\nTracker'))
    print(Style.RESET_ALL)



if __name__ == "__main__":
    detailText = []
    priceTracker = PriceTracker()
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
            elif selectedMenuOpt == 1:

                productURL = input("Product URL: ")
                #TODO ürünün URL bilgisinden hangi e-ticaret sitesinde olduğunu kontrol et
                productURL = "https://www.amazon.com.tr/SAMSUNG-SAPSI-Dahili-Sürücüsü-MZ-V8V1T0BW/dp/B08TJ2649W/ref=asc_df_B08TJ2649W/?tag=trshpngglede-21&linkCode=df0&hvadid=510610866222&hvpos=&hvnetw=g&hvrand=7595024957723860355&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9056794&hvtargid=pla-1187972384534&psc=1" # for testing
                
                productName = input("Product name: ")

                fiyatTakip = input("Ürünün fiyat bilgisini takip etmek istermisiniz? (e/h)")
                if "e" in fiyatTakip or "E" in fiyatTakip:
                    checkPrice = True
                else:
                    checkPrice = False
                    
                stokTakip = input("Ürünün stok bilgisini takip etmek istermisini? (e/h)")
                if "e" in stokTakip or "E" in stokTakip:
                    checkStock = True
                else:
                    checkStock = False
                productTime = time()
                product = Product(productName=productName,productURL=productURL,productTime=productTime,checkStock=checkStock,checkPrice=checkPrice)
                priceTracker.addProduct(product=product)
                detailText.append("ürün ekleme işlemi yapıldı")
        else:
            print(returnKey)




