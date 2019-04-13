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
        ## hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary
