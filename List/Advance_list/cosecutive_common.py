#https://www.geeksforgeeks.org/python-program-to-check-if-the-list-contains-three-consecutive-common-numbers-in-python/
#check if any three consecutive numbers are equal.


a = [1, 2, 2, 2, 3, 4, 5]

# using zip function
for x, y, z in zip(a, a[1:], a[2:]):
    if x == y == z:
        print(f"x : {x}")
        print("Found")
        break
else:
    print("Not Found")


#using for loop
for i in range(len(a)-2):
    if a[i] == a[i+1] == a[i+2]:
        print(f"Found in for loop. Start:{a[i]}, End:{a[i+2]}")
        break
    else:
        print(f"Not found in for loop Start:{a[i]}")