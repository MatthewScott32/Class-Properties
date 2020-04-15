
class Student:
    def __str__(self):
        return f"{self.full_name} is a student in cohort {self.cohort} and is {self.age} years old."

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return "nada"

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Must be a string')

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return "nada"

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else: 
            raise TypeError('Must be a string')

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return "nada"

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Must be an integer")

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return "nada"

    @cohort.setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else: 
            raise TypeError("Must be an integer")

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

student1 = Student()
student1.first_name = "Jimmy"
student1.last_name = "Smits"
student1.age = 32
student1.cohort = 100
print(student1.full_name)
print(student1)