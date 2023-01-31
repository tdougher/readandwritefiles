import csv
employeefile = 'EmployeePay.csv'
infile = open(employeefile, 'r', newline='')
reader = csv.reader(infile)
for row in reader:
    employee_id = row[0]
    employee_first = row[1]
    employee_last = row[2]
    salary = row[3]
    bonus = row[4]
    print(format(row[0], '3'), format(row[1], '12'), format(row[2], '15'), format(row[3], '6'), format(row[4], '4'))
 
infile.close()
