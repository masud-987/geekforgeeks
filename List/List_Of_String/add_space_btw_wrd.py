#https://www.geeksforgeeks.org/python-add-space-between-potential-words/

test_list = [ "gfgBest", "forGeeks", "andComputerScienceStudents"]

#using for loop

res = []
for elements in test_list:
    temp = [[]]
    for i in elements:
        if i.isupper():
            temp.append([])
        temp[-1].append(i)
    res.append(' '.join(''.join(ele) for ele in temp))

print(res)