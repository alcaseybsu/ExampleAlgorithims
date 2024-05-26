# heap_sprt.py
# Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. It is similar to selection sort, but it has a time complexity of O(n log n). The heap_sort.py snippet is shown below:

class heap_sort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n, -1, -1):
            self.heapify(n, i)
        for i in range(n-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(i, 0)
        return self.arr

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.arr[i] < self.arr[left]:
            largest = left
        if right < n and self.arr[largest] < self.arr[right]:
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)
            
print(heap_sort([5, 3, 8, 6, 7, 2]).sort())