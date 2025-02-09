#https://www.geeksforgeeks.org/python-program-to-swap-two-variables/

def swap_vars(x,y): #naive approach
    temp = x
    x = y
    y = temp
    return x,y

def swap_var_no_temp(x,y):
    x, y = y, x
    return x, y

#use substract operator
def swap_sub(x,y):
    x = x+y
    y = x-y
    x = x-y
    return x,y

if __name__ == "__main__":
    x=10
    y=30
    x, y = swap_vars(x,y)
    print(f"values of x {x} and y {y}")
 
    x, y = swap_var_no_temp(x,y)
    print(f"values of x {x} and y {y}")
 
    x, y = 15,39
    x, y = swap_sub(x,y)
    print(f"values of x {x} and value of y {y}")