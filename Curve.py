class Curve():
    def __init__(self, tenors, base_yield_curve):
        self.tenors = tenors
        self.base_yield_curve = base_yield_curve

    def get_disc_factor(self, spread):
        return (1 + self.base_yield_curve + spread) ** (-self.tenors)
    
    def bump_disc_factor(self, spread, bump):
        return (1 + self.base_yield_curve + spread + bump) ** (-self.tenors)