import json
import csv


#nfile = open("emp_data.json","r")
with open('emp_data.json') as json_data:

	employee_parsed = json.load(json_data)
	print employee_parsed
	

	emp_data = employee_parsed['employee_details']

	employ_data = open('EmployData.csv', 'w')

	csvwriter = csv.writer(employ_data)

	count = 0

for emp in emp_data:

	if count == 0:
		header = emp.keys()
		csvwriter.writerow(header)
		count += 1

	csvwriter.writerow(emp.values())

employ_data.close()


