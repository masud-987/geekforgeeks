#https://www.geeksforgeeks.org/python-ways-to-find-length-of-list/

def length(list):
    return(len(list))

#using for loop (naive method)
def length_for(list):
    count = 0
    for i in list:
        count += 1
    return count


a = [1,4,5,9]
len = length_for(a)
print(f"length of the list {len}")

