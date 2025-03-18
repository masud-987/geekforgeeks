##Brute force approach
# Time complexity: O(n^2), where n is the length of the list
# Auxiliary Space: O(n), extra space of size n is required
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

def uniq_items(list):
    uniq = []
    for i in list:
        if i not in uniq:
            uniq.append(i)
    
    return len(uniq)

total = uniq_items (input_list)
print(total)



#Using Counter in Python
#Counters are a subclass of the dict class in Python collections module
# Time complexity: O(n), where n is the length of input_list
# Auxiliary Space: O(n), extra space required for set.

from collections import Counter
items = Counter(input_list).keys()
print(f"Total uniq items {len(items)}")



#Using set
# Time complexity: O(n), where n is the length of input_list
# Auxiliary Space: O(n), extra space required for set.

new_set = set(input_list)
print(f"Total uniq items {len(new_set)}")



# converting our list to filter list
new_set = [ x for i, x in enumerate(input_list) if x not in input_list[:i]]
print("No of unique items in the list are:", len(new_set))