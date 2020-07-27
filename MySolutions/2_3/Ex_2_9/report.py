# report.py
#
# Exercise 2.9 & 2.10 & 2.11 & 2.12

import sys
import csv

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 1:
                prices[row[0]] = float(row[1])
    return prices

def read_portfolio(filename):
    ''' Report the total cost of a portfolio file'''

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    
    return portfolio

def make_report(portfolio, prices):
    report = []
    for name, share, price in portfolio:
        report.append((name, share, prices[name], prices[name]-price))
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ') * len(headers))
    for name, share, price, gain in report:
        newprice = '$%0.2f' % price
        print(f'{name:>10s} {share:>10d} {newprice:>10s} {gain:>10.2f}')
    return report

portfolio = read_portfolio('../../../Work/Data/portfolio.csv')
prices = read_prices('../../../Work/Data/prices.csv')
report = make_report(portfolio, prices)