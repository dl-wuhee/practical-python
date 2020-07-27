import sys
import csv

def portfolio_cost(pfilename):
    costs = 0.0
    f = open(pfilename, 'r')
    rows = csv.reader(f)
    headers = next(f)
    for rowno, row in enumerate(rows, start=1):
        try:
            costs = costs + int(row[1]) * float(row[2])
        except ValueError:
            print(f'Row {rowno}: Bad row:{row}')
    return costs

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '../../../Work/Data/missing.csv'

cost = portfolio_cost(filename)
print('Total cost %.2f'%cost)