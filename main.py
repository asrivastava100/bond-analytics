import numpy as np
from Curve import Curve
from Bond import Bond

def main():
    rates = np.array([0.01, 0.01, 0.01, 0.01, 0.01])
    tenors = np.arange(1, 6)
    curve = Curve(tenors, rates)
    cashflows = np.array([1,1,1,1,101])
    bond = Bond('', cashflows, tenors, 0)
    print(bond.price_bond(curve))

if __name__ == '__main__':
    main()


