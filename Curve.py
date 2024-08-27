class Curve():
    def __init__(self,tenors, rates):
        self.tenors = tenors
        self.rates = rates

    def get_disc_factor(self):
        return (1+self.rates)**(-self.tenors)