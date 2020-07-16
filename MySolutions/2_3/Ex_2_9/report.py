# report.py
#
# Exercise 2.7

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
    return report