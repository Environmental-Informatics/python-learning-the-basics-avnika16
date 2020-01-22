##Avnika Manaktala - Lab01- ABE65100

# Exercise 3.2 

def do_twice(f,v): #function to perform action twice
    f(v)
    f(v)

def print_twice(v): #function to print twice
    print(v)
    print(v)

do_twice(print_twice,'spam') #performing function do_twice
