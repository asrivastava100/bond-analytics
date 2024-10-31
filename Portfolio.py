import numpy as np
from Bond import Bond
from Curve import Curve

# assume each bond has the same currency / maturity / coupon frequency for now.
# look to extend the below to allow different values for the above

class Portfolio():
    def __init__(self, bond_portfolio = []) -> None:
        self.bond_portfolio = bond_portfolio
        self.curve = Curve(np.arange(1,6),np.array([0.01 for i in range(5)]))

    def add_bond(self,description,cashflows,tenors,spread):
        new_bond = Bond(description,cashflows,tenors,spread)
        self.bond_portfolio.append(new_bond)

    def run_prices(self):
        return [bond.price_bond(self.curve) for bond in self.bond_portfolio]
    
    def inspect_dv01s(self):
        return [bond.dv01(self.curve) for bond in self.bond_portfolio]

    def run_dv01s(self):
        return sum(self.inspect_dv01s())
    