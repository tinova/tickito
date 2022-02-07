# Created 06/09/2018 by reddit user anonananananabatman
# Made available under GNU GENERAL PRIVATE LICENSE
# ver 1.0

import time
import sys
import json
import requests
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()

# Display loading string
mylcd.lcd_display_string("Working...", 0)

# Create font for arrows
fontdata1 = [
    [0b00000,
	0b00100,
	0b00100,
	0b01110,
	0b01110,
	0b11111,
	0b11111,
	0b00000],

    [0b00000,
	0b11111,
	0b11111,
	0b01110,
	0b01110,
	0b00100,
	0b00100,
	0b00000],

    [0b00000,
	0b00100,
	0b01110,
	0b11111,
	0b00000,
	0b11111,
	0b01110,
	0b00100],

    [
        0b00110,
	0b01001,
        0b11100,
	0b01000,
	0b11100,
	0b01001,
	0b00110,
	0b00000],
    ]

# import font data
mylcd.lcd_load_custom_chars(fontdata1)

# set variables for last price of currency
lastPrice = 0
lastPriceEur = 0
lastPrice1 = 0
lastPrice2 = 0
lastPrice3 = 0
lastPriceDot = 0
lastPriceBnb = 0
lastPriceCake = 0
lastPriceDoge = 0

# Preload btc price before beginning while loop
def fetch_price(symbol, currency):
    try:
        queryParams = "fsym=" + symbol + "&tsyms=" + currency
        queryParams += "&api_key=01b724f29232b9cfecd00822b3b752b30e5a115bd19b9a6b46c96e72c28e909d"
        print( queryParams)
        b = requests.get("https://min-api.cryptocompare.com/data/price?" + queryParams)
        priceFloat = float(json.loads(b.text)[currency])
        return priceFloat
    except requests.ConnectionError:
        print ("Error querying Crytocompare API")

# Determines direction of the arrow
def arrow_dir(currentPrice):
    if lastPrice == currentPrice:
        return 2
    elif lastPrice > currentPrice:
       return 1
    elif lastPrice < currentPrice:
        return 0

# Determines direction of the arrow
def arrow_dir_btc_eur(currentPriceEur):
    if lastPriceEur == currentPriceEur:
        return 2
    elif lastPriceEur > currentPriceEur:
       return 1
    elif lastPriceEur < currentPriceEur:
        return 0

def arrow_dir_eth(currentPrice):
    if lastPrice1 == currentPrice:
        return 2
    elif lastPrice1 > currentPrice:
        return 1
    elif lastPrice1 < currentPrice:
        return 0

def arrow_dir_ltc(currentPrice):
    if lastPrice2 == currentPrice:
        return 2
    elif lastPrice2 > currentPrice:
        return 1
    elif lastPrice2 < currentPrice:
        return 0

def arrow_dir_dot(currentPrice):
    if lastPriceDot == currentPrice:
        return 2
    elif lastPriceDot > currentPrice:
        return 1
    elif lastPriceDot < currentPrice:
        return 0

def arrow_dir_bnb(currentPrice):
    if lastPriceBnb == currentPrice:
        return 2
    elif lastPriceBnb > currentPrice:
        return 1
    elif lastPriceBnb < currentPrice:
        return 0

def arrow_dir_cake(currentPrice):
    if lastPriceCake == currentPrice:
        return 2
    elif lastPriceCake > currentPrice:
        return 1
    elif lastPriceCake < currentPrice:
        return 0

def arrow_dir_doge(currentPrice):
    if lastPriceDoge == currentPrice:
        return 2
    elif lastPriceDoge > currentPrice:
        return 1
    elif lastPriceDoge < currentPrice:
        return 0

def arrow_dir_cro(currentPrice):
    if lastPriceCro == currentPrice:
        return 2
    elif lastPriceCro > currentPrice:
        return 1
    elif lastPriceCro < currentPrice:
        return 0

def arrow_dir_rose(currentPrice):
    if lastPriceRose == currentPrice:
        return 2
    elif lastPriceRose > currentPrice:
        return 1
    elif lastPriceRose < currentPrice:
        return 0

time.sleep(1)


while True:
    try:
        mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2)#, 0)
        
	# Writes BTC price to LCD
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ",0)
        time.sleep(0.4)
        btcPrice = fetch_price("BTC","USD")
        mylcd.lcd_display_string("$" + str(btcPrice) + "/BTC  ", 1)
        mylcd.lcd_write_char(arrow_dir(btcPrice))
        print("$" + str(btcPrice) + "/BTC " + str(arrow_dir(btcPrice)))
        lastPrice = btcPrice
    
        time.sleep(180)
       
        mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2)#, 0)
 
        # Writes BTC EUR price to LCD
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ",0)
        time.sleep(0.4)
        mylcd.lcd_write(0x80)
        mylcd.lcd_write_char(3)
        btcPriceEur = fetch_price("BTC","EUR")
        mylcd.lcd_display_string(str(btcPriceEur) + "/BTC  ", 0)
        arrow_dir_char = arrow_dir_btc_eur(btcPriceEur)
        mylcd.lcd_write_char(arrow_dir_char)
    
        print("€" + str(btcPriceEur) + "/BTC " + str(arrow_dir_char))
        lastPriceEur = btcPriceEur
    
        time.sleep(180)
    
        mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2)#, 0)
    
        # Writes ETH price to the LCD
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ", 0)
        time.sleep(0.4)
        mylcd.lcd_write(0x80)
        mylcd.lcd_write_char(3)
        ethPrice = fetch_price("ETH","EUR")
        mylcd.lcd_display_string(str(ethPrice) + "/ETH    ", 0)
        mylcd.lcd_write_char(arrow_dir_eth(ethPrice))
    
        print("€" + str(ethPrice) + "/ETH " + str(arrow_dir_eth(ethPrice)))
        lastPrice1 = ethPrice
    
        time.sleep(60)
    
        mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2)
    
        # Writes LTC price to the display
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ", 0)
        time.sleep(0.4)
        mylcd.lcd_write(0x80)
        mylcd.lcd_write_char(3)
        ltcPrice = fetch_price("LTC", "EUR")
        mylcd.lcd_display_string(str(ltcPrice) + "/LTC    ", 0)
        mylcd.lcd_write_char(arrow_dir_ltc(ltcPrice))
    
        print("€" + str(ltcPrice) + "/LTC " + str(arrow_dir_ltc(ltcPrice)))
        lastPrice2 = ltcPrice
    
        time.sleep(60)

        mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2)
    
        # Writes DOT price to the display
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ", 0)
        time.sleep(0.4)
        mylcd.lcd_write(0x80)
        mylcd.lcd_write_char(3)
        dotPrice = fetch_price("DOT", "EUR")
        mylcd.lcd_display_string(str(dotPrice) + "/DOT    ", 0)
        mylcd.lcd_write_char(arrow_dir_dot(dotPrice))
    
        print("€" + str(dotPrice) + "/DOT " + str(arrow_dir_dot(dotPrice)))
        lastPriceDot = dotPrice
 
        time.sleep(60)

        mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2)
    
        # Writes BNB price to the display
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ", 0)
        time.sleep(0.4)
        mylcd.lcd_write(0x80)
        mylcd.lcd_write_char(3)
        bnbPrice = fetch_price("BNB", "EUR")
        print(bnbPrice)
        mylcd.lcd_display_string(str(bnbPrice) + "/BNB    ", 0)
        mylcd.lcd_write_char(arrow_dir_bnb(bnbPrice))
    
        print("€" + str(bnbPrice) + "/BNB " + str(arrow_dir_bnb(bnbPrice)))
        lastPriceBnb = bnbPrice
 
        time.sleep(60)

        # Writes CAKE price to the display
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ", 0)
        time.sleep(0.4)
        mylcd.lcd_write(0x80)
        mylcd.lcd_write_char(3)
        cakePrice = fetch_price("CAKE", "EUR")
        print(cakePrice)
        mylcd.lcd_display_string(str(cakePrice) + "/CAKE   ", 0)
        mylcd.lcd_write_char(arrow_dir_cake(cakePrice))
    
        print("€" + str(cakePrice) + "/CAKE " + str(arrow_dir_cake(cakePrice)))
        lastPriceCake = cakePrice
 
        time.sleep(60)

        # Writes DOGE price to the display
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ", 0)
        time.sleep(0.4)
        mylcd.lcd_write(0x80)
        mylcd.lcd_write_char(3)
        dogePrice = fetch_price("DOGE", "EUR")
        print(dogePrice)
        mylcd.lcd_display_string(str(dogePrice) + "/DOGE   ", 0)
        mylcd.lcd_write_char(arrow_dir_doge(dogePrice))
    
        print("€" + str(dogePrice) + "/DOGE " + str(arrow_dir_doge(dogePrice)))
        lastPriceDoge = dogePrice
 
        time.sleep(60)

        # Writes CRO price to the display
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ", 0)
        time.sleep(0.4)
        mylcd.lcd_write(0x80)
        mylcd.lcd_write_char(3)
        croPrice = fetch_price("CRO", "EUR")
        print(croPrice)
        mylcd.lcd_display_string(str(croPrice) + "/CRO   ", 0)
        mylcd.lcd_write_char(arrow_dir_cro(croPrice))
    
        print("€" + str(croPrice) + "/CRO " + str(arrow_dir_cro(croPrice)))
        lastPriceCro = croPrice
 
        time.sleep(60)

        # Writes ROSE price to the display
        mylcd.lcd_write(0x80)
        mylcd.lcd_display_string("                ", 0)
        time.sleep(0.4)
        mylcd.lcd_write(0x80)
        mylcd.lcd_write_char(3)
        rosePrice = fetch_price("ROSE", "EUR")
        print(rosePrice)
        mylcd.lcd_display_string(str(rosePrice) + "/ROSE   ", 0)
        mylcd.lcd_write_char(arrow_dir_rose(rosePrice))
    
        print("€" + str(rosePrice) + "/ROSE " + str(arrow_dir_rose(rosePrice)))
        lastPriceRose = rosePrice
 
        time.sleep(60)

    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e)
        continue
