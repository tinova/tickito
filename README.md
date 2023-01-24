<div align="center">
  <a href="https://github.com/tinova/tickito">
    <img src="images/logo.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">tickito</h3>

  <p align="center">
    currency ticker that outputs price information of trade pairs on both a terminal and a raspberry 128x32 I2C display
    <br />
  </p>
</div>

## Ackowledgedments

* Logo found in Freepik by WangXiNa  (❤)

* Code based on ticker by anonananananabatman https://www.instructables.com/Cryptocurrency-Ticker/


## Requirements

### Hardware

* raspberry pi
* 128x32 I2C display

### Software

* python3 / pip3
* TrueType font, defaults to DejaVuSans.ttf, but it can be changed (see Configuration below). Needs to be installed in your system

### Ticker Source

You'll need an API key from [CyptoCompare](https://www.cryptocompare.com "CyptoCompare").

## Install

```sh
$ pip3 install adafruit-circuitpython-ssd1306 pyyaml
$ git clone https://github.com/tinova/tickito.git
$ cd tickito
 ```

## Configuration

There are three configuration parameters in lib/config.yaml

* cryptocompare_api_token needs to be set to your CryptoCompare API key
* font_for_display can be changed to your desired TrueType font (needs to be installed in your system)
* pairs is an array containing the trade pairs you want to display the price of. Each element of the array is a 3-tuple:

    ['TOKEN', 'CURRENCY', seconds-on-screen]

## Usage

```sh
$ python3 tickito.py
```
<hr>

Contributions are welcome!

<p align="right">(<a href="#readme-top">back to top</a>)</p>
