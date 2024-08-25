#1 Create two variables – one with your name and one with your age

name = input('Type in your name:')
age = int(input('Type in your age:'))

#2 Create a function which prints your data as one string

def print_data():
    statement  = '/n'+name+' '+str(age)+''
    print(statement)

print_data()

#3 Create a function which prints ANY data (two arguments) as one string

def greet():
    statement = '\nhello ' +name+ ', you are ' +str(age)+ ' years old'
    print(statement)

greet()



#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)

def decade():
    num = age // 10
    if age < 10:
        print("\nyou're younger than 10")
    else:
        print("\nyou have lived for "+str(num)+" decades")

decade()