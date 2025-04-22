class BinarySearch:
    def __init__(self, array, target):
        self.array  = array
        self.target = target
    
    def search_binary(self):
        #edge case: check if array is empty
        if not self.array:
            return -1

        start = 0
        end   = len(self.array) - 1

        while start <= end:
            mid = (start + end) // 2
            if self.array[mid] == self.target:
                return self.array[mid]
            elif self.array[mid] < self.target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

array = [1, 3, 5, 7, 9, 11, 13, 15]          
test = BinarySearch(array, 50)
print(test.search_binary())
