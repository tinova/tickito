from lib import pair
from lib import draw
import time
import requests
import json
import sys

# Get the arguments

if len(sys.argv) > 0 && sys.argv[1] == "-h":
    print("tickito fetches price pair updates and prints it to both the terminal and a i2c 128x32 raspberry attached OELD display"
    print(" - check http://github.com/tinova/tickito/README.md for the must haves")
    print(" - set the needed info in config/config.yaml")
    print(" - run tickito.py without arguments to start")
    sys.exit()

# Preload btc price before beginning while loop
def fetch_price(symbol, currency):
    try:
        queryParams = "fsym=" + symbol + "&tsyms=" + currency
        #queryParams += "&api_key=01b724f29232b9cfecd00822b3b752b30e5a115bd19b9a6b46c96e72c28e909d"
        queryParams += "&api_key=31a251f7abc9f1b4ae897800eb0316a77d77997a98bf1e9954f662b36089d738"
        b = requests.get("https://min-api.cryptocompare.com/data/price?" + queryParams)
        priceFloat = float(json.loads(b.text)[currency])
        return priceFloat
    except requests.ConnectionError:
        print ("Error querying Crytocompare API")

with open("config/config.yaml", "r") as yamlfile:
    config = yaml.load(yamlfile, Loader=yaml.FullLoader)

if (config["pairs"] is None or len(config["pairs"] < 1 or
    config['cryptocompare_api_token'] is None):
    print("config.yaml is malformed")
    sys.exit()

# Load the list of pairs
listOfPairs = []
for one_pair in config["pairs"]:
    base = one_pair[0]
    quote = one_pair[1]
    timeOnScreen = 60
    if not one_pair[2] is None:
        timeOnScreen = one_pair[2]
    listOfPairs.append(pair.Pair(base, quote, timeOnScreen))

# Initialize OLED screen
draw_oled = draw.Draw()

# Ready to go

puts "tickito starting ...\n"

# TODO: Is this needed?
# time.sleep(1)

while True:
    try:
        for pair in listOfPairs:
            print("fetching new price update for " + pair.base + "/" + pair.quote + ": ")
            newPrice = fetch_price(pair.base,pair.quote)
            draw_oled.showOnScreen(pair,newPrice)

        continue
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print("Exception in main loop")
        print(e)
        print(type(e))
        print("--------")
        # We sleep anyway to avoid API saturation on errors
        time.sleep(pair.timeOnScreen)
        continue
