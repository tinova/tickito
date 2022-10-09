# -------------------------------------------------------------------------- #
# Copyright 2022, tinova (https://github.com/tinova)                         #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#--------------------------------------------------------------------------- #


import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class Draw:
    """Draw on a 128x32 OLED I2C screen

    Format on the screen is limited to two sections


      Date Time

      [LOGO] CURRENCY_SYMBOL PRICE / TOKEN NAME

    Attributes:
        disp: Represents the OLED screen
        widthr width of the OLED screen
        height: height of the OLED scren
        draw: drawing object to draw on screen
        font: default font
    """

    def __init__(self):
        """ Initialize I2C iterface and clear OLED display."""
        # Create the I2C interface.
        i2c = busio.I2C(SCL, SDA)

        # Create the SSD1306 OLED class.
        # The first two parameters are the pixel width and pixel height.  Change these
        # to the right size for your display!
        self.disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

        # Clear display.
        self.disp.fill(0)
        self.disp.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new("1", (self.width, self.height))

        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)


        # Load default font.
        self.font = ImageFont.load_default()

        # Alternatively load a TTF font.  Make sure the .ttf font file is in the
        # same directory as the python script!
        # Some other nice fonts to try: http://www.dafont.com/bitmap.php
        # font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)


    def showOnScreen(self, pair, newPrice):
        padding = -2
        top = padding
        bottom = self.height - padding

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        # Draw time
        self.draw.text((0, top+0), time.strftime("%H:%M:%S    %m/%d/%y"), font=self.font, fill=255)

        # Draw ticket value on screen
        self.draw.text((0, top+25), "     $" + str(newPrice) + "/" + pair.base + " ", font=self.font, fill=255)

        # Output to stdout for debugging
        print("$" + str(newPrice) + "/" + pair.base + " " + str(pair.arrow_dir(newPrice)) + "\n")

        # Update price of the pair
        pair.lastPrice = newPrice

        # Show image
        self.disp.image(self.image)
        self.disp.show()

        # Leave it showing for 'timeOnScreen' seconds
        time.sleep(pair.timeOnScreen)
