
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def move(self):
        print("person is walking")


person1 = Person("mike",21,'male')
person2 =Person('juliet',23,'female')
person3 = Person('koech',22,'male')
print(person1.name)
print(person2.age)
print(person2.gender)


