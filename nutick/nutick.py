import pair
import draw
import time
import requests
import json

# Preload btc price before beginning while loop
def fetch_price(symbol, currency):
    try:
        queryParams = "fsym=" + symbol + "&tsyms=" + currency
        queryParams += "&api_key=01b724f29232b9cfecd00822b3b752b30e5a115bd19b9a6b46c96e72c28e909d"
        b = requests.get("https://min-api.cryptocompare.com/data/price?" + queryParams)
        priceFloat = float(json.loads(b.text)[currency])
        return priceFloat
    except requests.ConnectionError:
        print ("Error querying Crytocompare API")

# Define currency pairs Array
listOfPairs = []

listOfPairs.append(pair.Pair("BTC","USD",120))
listOfPairs.append(pair.Pair("BTC","EUR",60))
listOfPairs.append(pair.Pair("ETH","EUR",60))
listOfPairs.append(pair.Pair("DOT","EUR",30))
listOfPairs.append(pair.Pair("BNB","EUR",60))
listOfPairs.append(pair.Pair("DOGE","EUR",60))
listOfPairs.append(pair.Pair("CRO","EUR",60))
listOfPairs.append(pair.Pair("ROSE","EUR",60))

# Initialize OLED screen
draw_oled = draw.Draw()

# TODO: Is this needed?
time.sleep(1)

while True:
    try:
        for pair in listOfPairs:
            newPrice = fetch_price(pair.base,pair.quote)
            draw_oled.showOnScreen(pair,newPrice)

        continue
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e)
        continue
