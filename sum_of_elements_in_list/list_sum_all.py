class ListSum:
    def __init__(self, list_to_be_summed):
        self._list = list_to_be_summed
    
    def sum(self):
        total = self._list[0]
        for ele_in_list in self._list[1:]:
            total = total + ele_in_list
        return total

    #add using recurssion
    
    #using while loop
    
    #sum method
    
    #add funtions
    
    #using enumuration
    
    #using list comprehensiton
    
    #using lambda functuion
    
    #using add operator


item = [1,2,3,4,5]
client = ListSum(item)
print(client.sum())
