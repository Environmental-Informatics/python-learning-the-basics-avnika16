##Avnika Manaktala - Lab01- ABE65100

##Exercise 3.3 

print("Part 1: Printing a 2x2 grid") #Title

def do_twice(f): # defining function to do action twice 
    f()
    f()
    
def do_four(f): # defining function to do action four times 
    do_twice(f)
    do_twice(f)
  
#Creating horizontal beams for the grid
row= '+ - - - - '    
def print_row():
   print (row*2, '+') 

#Creating vertical columns for the grid
col= '|         '  
def print_col():
    print(col*2 , '|') 

def print_hor(): #Function to create individual rows
    print_row()
    do_four(print_col)
    
def print_grid(): #Assembling the whole grid
    do_twice(print_hor)
    print_row()
    
print_grid() #Displaying grid

print("Part 2: Printing a 4x4 grid") #Title

#Creating horizontal beams for the grid
row= '+ - - - - '    
def print_4row():
   print (row*4, '+') 

#Creating vertical columns for the grid
col= '|         '  
def print_4col():
    print(col*4 , '|') 

def print_4hor(): #Function to create individual rows
    print_4row()
    do_four(print_4col)
    
def print_grid(): #Assembling the whole grid
    do_four(print_4hor)
    print_4row()
    
print_grid() #Displaying grid