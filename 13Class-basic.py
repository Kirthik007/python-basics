"""Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

"""
class Samp :
    def walk(self):
        print("walks ")
        print("from inside walks func ")
    x = 7
a = Samp()
print(a)   #here just a class string is displayed useless
a.walk() #this line access walk func inside  Samp
print('\n',a.x)
a.x = 17#update x
print('updated ' ,a.x)

class Test:
    def __init__(self,n,c):
        self.name = n
        self.city = c
    def intro(self):
        print(f' Hi hello to all I am {self.name} from {self.city} \n')

j = Test('john','goa')
j.intro()
bob = Test('bob','ahamada ')
bob.intro()

#class inheritance
class Welc(Test):
    def mo(self):
        print(f' From Welc class {self.name} details ')
p = Welc('kong','island')
p.intro()
p.mo()

    
    
    
