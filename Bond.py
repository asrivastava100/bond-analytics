import numpy as np
from Curve import Curve

class Bond():
    def __init__(self,description,cashflows,tenors,spread) -> None:
        self.description = description
        self.cashflows = cashflows
        self.tenors = tenors
        self.spread = spread

    def price_bond(self, curve: Curve):
        disc_factors = curve.get_disc_factor()
        price = np.sum(self.cashflows * disc_factors)
        return price

