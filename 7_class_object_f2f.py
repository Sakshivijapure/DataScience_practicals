file=open("./employee.txt")

fileText=file.read()

records=fileText.split("\n")

file.close()

employeeList=[]

class Employee:
	def __init__(self,name,gender,location,salary):
		self.name = name
		self.gender = gender
		self.location = location  # Use lowercase
		self.salary = salary
		
for i in range(1,len(records)-1):
	recordDetails=records[i].split(",")
	empName=recordDetails[0]
	empGender=recordDetails[1]
	empLocation=recordDetails[2]
	empSalary=recordDetails[3]
	
	empObject=Employee(empName,empGender,empLocation,empSalary)
	'''empObject.name=empName
	empObject.gender=empGender
	empObject.location=empLocation
	empObject.salary=empSalary
	'''
	employeeList.append(empObject)
	
def totalSalaryToBePaid(empList):
	totalSalary=0
	for emp in empList:
		totalSalary=totalSalary+int(emp.salary)
	return totalSalary
def genderBaseSalary(empList):
	maleSalary=0
	femaleSalary=0
	for emp in empList:
		if emp.gender=="male":
			maleSalary+=int(emp.salary)
		elif emp.gender=="female":
			femaleSalary+=int(emp.salary)
	return{"male salary":maleSalary,"female salary":femaleSalary}
print(totalSalaryToBePaid(employeeList))
print(len(employeeList))
print(genderBaseSalary(employeeList))
