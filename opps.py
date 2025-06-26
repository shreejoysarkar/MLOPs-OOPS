class Employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary =  500000
        self.designation = 'SDE'

    # function defined under class "METHOD"
    def travel(self, destination):
        print('Employee is traveling to', destination)


# creating object/instance of Employee class

sam = Employee()

print(sam.id)
print(sam.salary)

print(sam.travel('New York'))