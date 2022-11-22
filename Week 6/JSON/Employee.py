import json
# creating employee data
a = { "Name":"R. Ashwin","DOB": "20-03-1997","Height" : 5.4,"City":"Mumbai","State":"Maharashtra"}

b = { "Name":"Mayuri","DOB": "11-07-1992","Height" : 5.2,"City":"Nagpur","State":"Maharashtra"}

c = { "Name":"Shreyash","DOB": "25-04-1989","Height" : 5.8,"City":"Udupi","State":"Karnataka"}

d = { "Name":"Reena","DOB": "14-01-1986","Height" : 5.4,"City":"Mangalore","State":"Karnataka"}

e = { "Name":"Puja","DOB": "27-11-1995","Height" : 5.2,"City":"Ranchi","State":"Jharkhand"}

employee_list = [] #creating empty list

#adding the data to the list
employee_list.append(a)
employee_list.append(b)
employee_list.append(c)
employee_list.append(d)
employee_list.append(e)

with open("employee.json","w") as file: # creating json file
    json.dump(employee_list,file)


with open("employee.json","r") as new_file: #reading json file and storing it
    new = json.load(new_file)

for i in new: #printing the employee data individually
    print(i)