class adult:
    def __init__(self, name, age ,weight):
        self.name=name
        self.age=age
        self.weight=weight
        try:
            lastblank= name.rindex(' ')
            self.lastname=name [lastblank +1 :]
        except:
            self.lastname=name

    def intro_self(self):
        print "My name is " + self.name
        print "last Name " + self.lastname


class child(adult):
    def fav_cartoon(self, cart):
        self.cart=cart

    def print_child(self):
        print ("My fav cartoon is {}".format(self.cart) )


p1= adult("Ali khan", 20 , 65)
p1.intro_self()

chil= child ("Nice Kid",14 , 30)
chil.intro_self()
chil.fav_cartoon("Johnny Bravo")

chil.print_child()
