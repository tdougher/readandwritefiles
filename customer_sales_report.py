import csv

infile = open("sales.csv", "r", newline="")
outfile = open("salesreport.csv", "w")
reader = csv.reader(infile)
writer = csv.writer(outfile, delimiter=",")
next(reader)
grand_total = 0
cust_id = ""
for row in reader:
    if row[0] != cust_id:
        outfile.write(cust_id + "," + str(grand_total) + "\n")
        cust_id = row[0]
        grand_total = 0
    subtotal = float(row[3])
    tax = float(row[4])
    shipping = float(row[5])
    total = subtotal + tax + shipping
    grand_total += total
infile.close()
outfile.close()
