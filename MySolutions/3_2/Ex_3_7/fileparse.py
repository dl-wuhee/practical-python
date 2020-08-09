# fileparse.py
import csv

def parse_csv(filename, separator=',', has_headers=True, select=None, types=None, silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=separator)

        # Read the file headers
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
        else:
            if select:
                indices = select
            else:
                indices = []

        records = []
        for n, row in enumerate(rows):
            if not row:
                continue
            if indices:
                try:
                    row = [row[index] for index in indices]
                except TypeError as e:
                    return None
#                    break
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {n} :', e)
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        
    return records

