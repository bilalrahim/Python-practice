

class over:
    def __init__(self, name):
        self.name=name

    def __repr__(self):


        print ("{} Successful !".format(self.name))
        return self.name



ob=over("good")
print (ob)

x = raw_input("Enter your name:")
print("Hello, " + x)
