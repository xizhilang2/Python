## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## is-a
class Dog(Animal):

    def __init__(self, name):
        ## has-a
        self.name = name

## is-a
class Cat(Animal):
    """docstring for Cat."""

    def __init__(self, name):
        super(Cat, self).__init__()
        ## has-a
        self.name = name

##
class Person(object):

    def __init__(self, name):
        ## has-a
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

##
class Employee(Person):

    def __init__(self, name, salary):
        ## is-a hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary

## is-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## is-a
santan = Cat("Santan")

## is-a
mary = Person("Mary")

## has-a
mary.pet = santan

## is-a
frank = Employee("Frank", 120000)

## has-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()
