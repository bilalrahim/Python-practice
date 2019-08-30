nameHandle= open('kids','w')
for i in range(2):
    name=raw_input('Enter Name :')
    nameHandle.write(name +'/n')
nameHandle.close()
