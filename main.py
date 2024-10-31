import numpy as np
from Curve import Curve
from Bond import Bond
from Portfolio import Portfolio

def main():
    # testing Bond, Curve & Portfolio classes
    rf_rates = np.array([0.01, 0.01, 0.01, 0.01, 0.01])
    spread = 0.05
    tenors = np.arange(1, 6)
    curve = Curve(tenors,rf_rates)
    cashflows = np.array([1,1,1,1,101])
    bond = Bond('', cashflows, tenors,spread)
    print(bond.price_bond(curve))
    print(bond.dv01(curve))

    portfolio_1 = Portfolio()
    portfolio_1.add_bond("abc",cashflows,tenors, 0.07)
    portfolio_1.add_bond("bcd",cashflows,tenors, 0.042)

    for bond in portfolio_1.bond_portfolio:
        print(bond)

    print(portfolio_1.run_prices())
    print(portfolio_1.run_dv01s())

if __name__ == '__main__':
    main()


