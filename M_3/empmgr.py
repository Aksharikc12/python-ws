from employee import Employee
'''
emp_1 = Employee(1,"Sunny","M.Tech",56000,"CS")
emp_2 = Employee(2,"Bunny","M.Tech",56000,"IS")

emp_1.show_info()
emp_2.show_info()
emp_1.increment_salary(2000)
emp_1.show_info()
emp_2.show_info()
'''


lst_emp=[]

def load_emp():
    with open("empdata.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            edata = data.strip("\n").split(",")
            empno = int(edata[0])
            ename = edata[1]
            qualification = edata[2]
            salary = int(edata[3])
            dept_name = edata[4]
            emp = Employee(empno, ename, qualification, salary, dept_name)
            lst_emp.append(emp)
    print(f"Total Employees count : {len(lst_emp)}")

def showDeptNames():
    dnames = set(map(lambda emp:emp.dept_name, lst_emp))
    for name in dnames:
        print(name)

def showAllQualifications():
    qualifications = set(map(lambda emp:emp.qualification, lst_emp))
    for qual in qualifications:
        print(qual)

def maxSalaryEmp():
    sal = max(list(map(lambda emp:emp.salary, lst_emp)))
    lst = list(filter(lambda x : x.salary == sal,lst_emp)) 
    for emp in lst:
        emp.show_info()   

def showEmpCountByDeptName():
    pass

def showTotalSalByDeptName():
    pass

def showEmpCountByQual():
    pass

load_emp()
print("All Dept name")
showDeptNames()
print("All qualifications")
showAllQualifications()
print("Max Salary Employees")
maxSalaryEmp()