import sys
import csv

def portfolio_cost(pfilename):
    costs = 0.0
    f = open(pfilename, 'r')
    rows = csv.reader(f)
    headers = next(f)
    for row in rows:
        costs = costs + int(row[1]) * float(row[2])
    return costs

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '../../../Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost %.2f'%cost)