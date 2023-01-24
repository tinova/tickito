# -------------------------------------------------------------------------- #
# Copyright 2022, tinova (https://github.com/tinova)                         #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#--------------------------------------------------------------------------- #

class Pair:
    """A Pair represents a token (base) valued in another token (quote)

    Attributes:
        base: base token of the pair
        quote: currency used to quote base price
        timeOnScreen: amount of seconds the pair will be shown
        lastPrice: last known price of thhe base token expressed in quote currency
    """

    def __init__(self, base=0, quote=0, timeOnScreen=0):
        """ Inits a Pair with initial values."""
        self.base = base
        self.quote = quote
        self.timeOnScreen = timeOnScreen
        self.lastPrice = 0

    # Determines direction of the base token current price
    # with respect to the previous price knownn

    def arrow_dir(self, newPrice):
        """ Calculates the direction of the price

        Args:
            newPrice: Current pair price

        Returns:
            0 if price is going up
            1 if price is going down
            2 if price remains the same
        """
        if self.lastPrice == newPrice:
            return "◆"
        elif self.lastPrice > newPrice:
            return "▼"
        elif self.lastPrice < newPrice:
            return "▲"
