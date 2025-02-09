#Python program to interchange first and last elements in a list
#https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/


#using a temp variable
def swap(list):
    temp = list[0]
    list[0] = list[-1]
    list[-1] = temp
    print(list)


#using multiple assignment

def swap_mul(list):
    list[0], list[-1] = list[-1], list[0]
    print("In swap mul")
    print(list)

if __name__ == "__main__":
    num = [1,10,100,50]
    swap_mul(num)