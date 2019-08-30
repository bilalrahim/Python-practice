#Think about all the possible inputs a user can enter which would result into error,
# well if not all most.
#instead of your program stalling it can show error thats the beauty of exception handling. 

def sumDigit(s):
    if isinstance(s, basestring):
        new_list=[int(i) for i in s if i.isdigit()]

        total = 0
        for x in new_list:
            total+=x
        print total
    else:
        raise Exception("Not A String")
#Method 2

def sumDigit(s):
    assert (isinstance(s,basestring)), "NOT A STRING"
    lis=[int(x) for x in s if x.isdigit()]
    print lis
sumDigit("12312")





def int_sq(val):
    while True:

        try:
            val=int (val)
            print 'The square is : ', val**2
            break
        except ValueError:
            print val , "NOT an integer"

int_sq("tets")



def findAnEven(l):
    flag=0
    for i in l:
        if i % 2 == 0:
            flag = 1
            print i
            break
    if flag == 0:
        raise Exception("NO EVEN NUMBERS IN LIST")

findAnEven([1,3,5])
