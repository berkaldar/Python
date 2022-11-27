file = open("employees.txt", "a+")

employees = int(input("Çalışan Sayısı: "))

employee = []

for i in range(0, employees):
    employeeName = input("Çalışan Adı: ")
    employeeLastName = input("Çalışan Soyadı: ")
    employeeSalary = float(input("Çalışan Maaşı "))
    employee.append(f"{employeeName} {employeeLastName} - {employeeSalary}")

    print(i)

file.writelines("\n" [employees])

print(file.read())
file.close()