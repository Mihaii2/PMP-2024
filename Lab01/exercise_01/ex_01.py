import csv
import numpy as np

with open('./some_list.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    students_indexes = np.random.choice(range(12), size=4, replace=False)

    i=0
    for row in csv_reader:
        if i in students_indexes:
            print(row)
        i += 1