## price.py

## Exercise 2.6

import csv

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 1:
                prices[row[0]] = float(row[1])
    return prices