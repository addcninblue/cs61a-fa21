import random

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    # funcs

class Dog(Pet):
    def talk(self):
        print("WOOF")

    @classmethod
    def robo_factory(cls, owner):
        return cls("RoboDog", owner)

class HomeDog(Dog):
    pass

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives

    @classmethod
    def adopt_random_cat(cls, owner):
        """return a new instance of cat with a randomly chosen name and a random number of lives"""
        cat_name = random.choice(['felix', 'bugs', 'grumpy'])
        num_lives = random.randint(1, 20)
        return cls(cat_name, owner, num_lives)

class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        """08/17"""
        month = int(date_string[:2])
        day = int(date_string[-2:])
        return cls(month, day)

    @staticmethod
    def access_class_variable(date_string):
        """08/17"""
        month = int(date_string[:2])
        day = int(date_string[-2:])
        return cls(month, day)

class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
         return self.x

    def __str__(self):
         return self.x * 2

class B:
    def __init__(self):
         print('boo!')
         self.a = []

    def add_a(self, a):
         self.a.append(a)

    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret
