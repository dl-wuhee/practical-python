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

def read_portfolio(stockfilename, pricefilename):
    ''' Report the total cost of a portfolio file'''

    portfolio = []

    prices = read_prices(pricefilename)

    with open(stockfilename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'Name': row[0],
                'Shares': int(row[1]),
                'Price': float(row[2]),
                'Change': prices[row[0]] - float(row[2])
            }
            portfolio.append(holding)
    
    return portfolio

if len(sys.argv) == 3:
    stockfilename = sys.argv[1]
    pricefilename = sys.argv[2]
else:
    stockfilename = '../../../Work/Data/portfolio.csv'
    pricefilename = '../../../Work/Data/prices.csv'


portfolio = read_portfolio(stockfilename, pricefilename)