import csv

custfile = "customers.csv"
tempfile = "customers_country.csv"

# customers
infile = open(custfile, "r", newline="")
outfile = open(tempfile, "w", newline="")
writer = csv.writer(outfile, delimiter=",")
reader = csv.reader(infile)
for row in reader:
    new_row = [row[1], row[2], row[4]]
    writer.writerow(new_row)

infile.close()
outfile.close()
