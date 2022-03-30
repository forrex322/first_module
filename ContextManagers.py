import csv

filename = 'test.csv'

print('Writing to file')

header = ['Name; Age']
data = [[f'Alex; {18}'], [f'Dima; {20}'], [f'Oleg; {24}']]

with open(filename, 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(data)

print('Reading from file')

rows = []
with open(filename, 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        rows.append(row)
        print(row)
print(rows)

print('Appending to file')

data2 = [[f'Maks; {22}'], [f'Vova; {20}']]
with open(filename, 'a', newline='') as file:
    csvappender = csv.writer(file)
    csvappender.writerows(data2)
