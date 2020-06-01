'''
A rubber ball is dropped from a height of 100 meters and each time it hits
the ground, it bounces back up to 3/5 the height it fell. Write
a program bouce.py that prints a table shwing the height of the first 10 bouces.
'''

height = 100.0  # Meter
bouce_ratio = 3.0 / 5.0
num_bouce = 1

while num_bouce < 11:
    height = height * bouce_ratio
    print(num_bouce, round(height, 4))
    num_bouce = num_bouce + 1

    