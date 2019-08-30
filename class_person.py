#Classes in python : Classes allows you to create your own data type
#You can store information in it in just the way you want.

class person:
    def __init__(self, x , age):
        self.name=x
        self.age=age

    def selname(self):
        print ("Hello my name is " + self.name)



p1=person ("Ali", 50)

p1.selname()


name = "Ali khan"
lastblank= name.rindex(" ")

print lastblank

lastname = name[lastblank +1 :]

print lastname

print type(p1)
