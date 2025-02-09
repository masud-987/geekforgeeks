test_list = [ "gfgBest", "forGeeks", "andComputerScienceStudents"]

#using for loop

res = []
for elements in test_list:
    temp = [[]]
    for i in elements:
        if i.isupper():
            temp.append([])
        temp[-1].append(i)
    for t in temp:
        print("In temp")
        res += "".join(t)
        print(res)
