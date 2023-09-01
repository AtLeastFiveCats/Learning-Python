import csv
import os

with open("files\cile.csv", "w", newline="") as f:
    data_handle = csv.writer(f, delimiter=",")
    data_handle.writerow(["Food", "Easy", "Rating"])
    data_handle.writerow(["Pizza", "Yes", "10"])
    data_handle.writerow(["Taco", "No", "8"])
with open("files\cile.csv", "a", newline="") as f:
    data_reader = csv.writer(f, delimiter=",")
    data_reader.writerow(["Salad", "Yes", "8"])
with open("files\cile.csv") as f:
    row = csv.reader(f)
    list = []
    for data in row:
        list += data
print(list)