# quick_sort.py

class quick_sort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        if len(self.arr) <= 1:
            return self.arr
        else:
            pivot = self.arr.pop()
            greater = []
            lesser = []
            for i in self.arr:
                if i > pivot:
                    greater.append(i)
                else:
                    lesser.append(i)
            return quick_sort(lesser).sort() + [pivot] + quick_sort(greater).sort()
        
        print(sort([5, 3, 8, 6, 7, 2]).sort())