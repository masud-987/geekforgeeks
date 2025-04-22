#https://www.geeksforgeeks.org/python-program-to-check-if-the-list-contains-three-consecutive-common-numbers-in-python/
#check if any three consecutive numbers are equal.

a = [1,2,3,4,5,6,7,8,9,10]
array_identical = [1,1,1,2,3]

x,y,*z = zip(a, a[1:], a[2:])
print(a, a[1:], a[2:])
print(x,y,z)

# first_3 = array[0:3]
# print(first_3)
