import numpy as np
from Curve import Curve

class Bond():
    def __init__(self, description, cashflows, tenors, spread) -> None:
        self.description = description
        self.cashflows = cashflows
        self.tenors = tenors
        self.spread = spread
        
    def pv_calculate(self, curve: Curve, apply_bump = False, bump = 0.0):
        disc_factors = curve.bump_disc_factor(self.spread, bump) if apply_bump else curve.get_disc_factor(self.spread) 
        discounted_pv = np.sum(self.cashflows * disc_factors)
        return discounted_pv
    
    def price_bond(self,curve: Curve):
        return self.pv_calculate(curve)
    
    def dv01(self,curve: Curve):
        bond_price = self.price_bond(curve)
        bumped_bond_price = self.pv_calculate(curve, True, 0.01)
        return bumped_bond_price - bond_price
    
    def __str__(self):
        return f"Description:{self.description},Spread:{self.spread},Tenors:{self.tenors},Cashflows:{self.cashflows}"
    