from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward:
    def __init__(self, name):
        self._name = name
        self._list_people = list()

    def add_person(self, person):
        self._list_people.append(person)

    def describe(self):
        print(f"Ward: {self._name}")
        for p in self._list_people:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self._list_people:
            if isinstance(p, Doctor):
                count += 1
        return count

    def sort_age(self):
        self._list_people.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        count = 0
        total_year = 0
        for p in self._list_people:
            if isinstance(p, Teacher):
                count += 1
                total_year += p.get_yob()
        return total_year / count


# 2(a)
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()


# 2(b)
print()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print(f"\nNumber of doctors: {ward1.count_doctor()}")

# 2(d)
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

# 2(e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")


teacher1 = Teacher(name ="teacherZ2023", yob = 1991, subject ="History")
teacher1.describe()
