#using join function
test_list = ["gfgBest", "forGeeks", "andComputerScience"]
new_list = " ".join(test_list)
print(type(new_list))



#using for loop
res = ""
for str in test_list:
    res += str + " "
print(f"Printing res ::: {res}")

