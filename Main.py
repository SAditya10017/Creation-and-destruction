# Write a program to create a class with the name employee and create
#  a constructor and destructor.
#  Then, create an object for that class and delete the object.


class employees:
    def __init__(self,age_required,experience_required):
        self.experience_required = experience_required
        self.age_required = age_required
    def display(self):
        print(self.age_required)
        print(self.experience_required)
    def __del__(self):
        print("Unemployed ike 99% of Gen Z")
E1 = employees(age_required=21,experience_required='phd')
E1.display()
del E1