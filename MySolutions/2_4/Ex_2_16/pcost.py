import sys
import csv

def portfolio_cost(pfilename):
    costs = 0.0
    f = open(pfilename, 'r')
    rows = csv.reader(f)
    headers = next(rows)
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            costs += nshares * price
        except ValueError:
            print(f'Row {rowno}: Bad row:{row}')
    return costs

filename = 'Work/Data/portfoliodate.csv'
cost = portfolio_cost(filename)
print('Total cost %.2f'%cost)