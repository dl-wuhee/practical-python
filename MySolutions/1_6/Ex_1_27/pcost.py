costs = 0.0
with open('../../../Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        costs = costs + int(row[1]) * float(row[2])

print('Total cost %.2f'%costs)