#https://www.geeksforgeeks.org/python-extract-elements-with-frequency-greater-than-k/

# Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
# Output : [4, 3] 
# Explanation : Both elements occur 4 times. 

from typing import List


class FindFrequency:
    def __init__(self, input_list: List[int]):
        self.input_list = input_list

        
    def sorting(self, k: int) -> List:
        self.input_list.sort()
        item_frequency = {}
        output = []
        for i in self.input_list:
            if i not in item_frequency:
                item_frequency[i] = 1
            else:
                item_frequency[i] += 1

            if item_frequency[i] == k+1:
                output.append(i)

        return output



items = [4, 6, 4, 3, 3, 4, 3, 3, 4, 3, 4, 3, 8, 8, 6, 8]
items.sort()
sol = FindFrequency(items)
output = sol.sorting(1)
print(output)