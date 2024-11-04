class Animal:
    def speak(self):
        print('animal is speaking')


class Dog(Animal):
    def bark(self):
        print('dog is barking')


dogObj = Dog()
dogObj.bark()
dogObj.speak()