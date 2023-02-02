class ListSum:
    def __init__(self, list_to_be_summed):
        self._list = list_to_be_summed
    
    #using for loop
    def sum_for_loop(self):
        total = self._list[0]
        for ele_in_list in self._list[1:]:
            total = total + ele_in_list
        return total

    #add using recurssion
    
    
    #using while loop
    def sum_while_loop(self):
        while_control_var = len(self._list) - 1
        total = self._list[0]
        while while_control_var > 0:
            total = total + self._list[while_control_var]
            while_control_var = while_control_var - 1
        return total
    
    #sum method
    
    #add funtions
    
    #using enumuration
    
    #using list comprehensiton
    
    #using lambda functuion
    
    #using add operator


item = [1,2,3,4,5]
client = ListSum(item)
print(client.sum_while_loop())
