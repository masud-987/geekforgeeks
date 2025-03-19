
#https://www.geeksforgeeks.org/python-list-product-excluding-duplicates/
from typing import List
from collections import Counter

#using set
class Solution:
    def uniq_product(self, nums: List[int]) -> int:
        self.no_duplicate = set(nums)
        self.res = 1
        for i in self.no_duplicate:
            self.res *= i
        return self.res

# new_obj = Solution()
# total = new_obj.uniq_product([1,2,3,3,3,3])
# print(total)


#using counter
class SolutionCounter():
    def uniq_counter(self, nums: List[int]) -> int:
        self.no_duplicate = Counter(nums).keys()
        self.res = 1
        for i in self.no_duplicate:
            self.res *= i
        return self.res



new_obj = SolutionCounter()
total = new_obj.uniq_counter([1,2,2,5,3,3,3,3])
print(total)



#Using dict.fromkeys()
a = [1,2,2,5,3,3,3,3]
# Unique Elements
uniq_vals = dict.fromkeys(a,"hi")
res = 1
for i in uniq_vals:
    res *= i

print(res)
