class Human:

    def __init__(self, first, last, gender):
        self.firstname = first
        self.lastname = last
        self.gender = gender

    def Name(self):
        return self.firstname + " " + self.lastname
    def Gender(self):
        return self.gender

class Employee(Human):

    def __init__(self, first, last, id):
        Human.__init__(self,first, last, gender, id, company, salary)
        self.id = id
        self.company=company
        self.salary=salary

    def GetEmployee(self):
        return self.Name()+ ", " +  self.company

x = Human("Raha", "Rohan", "Male")
y = Employee("Kumar", "Satish", "Male", "1007", "abc", "109000")

for i in self.salary:
print sorted(self.GetEmployee() key=lambda x:x[-1])
