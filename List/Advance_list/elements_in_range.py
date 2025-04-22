#https://www.geeksforgeeks.org/python-test-if-list-contains-elements-in-range/
## Check if List contains an elements in Range provided.

array = [10,20,30,15,5]

start = 50
end = 60
in_range = False


### using for loop
for i in array:
    if start <= i <= end:
        in_range = True
        break
print(in_range)



#using any() function
#The any() function returns True if any item in an iterable are true, 
# otherwise it returns False.
in_any = any(start <= num <= end for num in array)
print(in_any)




## above solution in the class

class Solution:
    def __init__(self, array, start, end):
        self.array    = array
        self.start    = start
        self.end      = end
        self.in_range = False

    def check_in_range(self):
        for i in self.array:
            if self.start <= i <= self.end:
                self.in_range = True
        
        return self.in_range

    def check_in_range_any(self):
        self.in_range = any(self.start <= i <= self.end for i in array)
        return self.in_range

check = Solution(array,start,end)
store = check.check_in_range_any()

print(f"value from the class {store}")

