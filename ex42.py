##amimal is a obhect (yes,sort of confusing )look at the e
class Animal(object):
    pass

## ??
class Dog(Animal):

    def _init_(self,name):
        ## ??
        self.name=name
## ??

class Cat(Animal):

    def _init_(self,name):
        ## ??
        self.name=name
## ??
class Person(object):

    def _init_(self,name):
        ## ??
        self.name=name

        ## person has a pet of some kind
        self.pet=None
## ??
class Employee(Person):

    def _init_(self,name,salary):
        ## ?? hmm what is this strange magic?
        super(Employee,self)._init_(name)
        ## ??
        self.salary=ssalary
 ## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover is a dog
rover=Dog("Rover")

## ??
satan=Cat("Satan")

## ??
eimon=Person("EiMon")

## ??
eimon.pet=satan

## ??
frank=employee("Frank",120000)

## ??
frank.pet=rover

## ??
flipper=Fish()

## ??
crouse=Salmon()

## ??
harry=Halibut()


