from Person import Person

class Student(Person):
    def __init__(self, p_name, p_age,p_height,p_major):
        super().__init__(p_name,p_age,p_height)
        self.major = p_major
        print("This time its a student object")


student1 = Student("John","25",22,"Computing")
print("The student name is: " + str(student1.name))
print("The student major is: " + str(student1.major))