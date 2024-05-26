# insertion_sort.py
# Insertion Sort algorithm in Python
#
class insertion_sort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i-1
            while j >= 0 and key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key
        return self.arr
        
print(insertion_sort([5, 3, 8, 6, 7, 2]).sort())