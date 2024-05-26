# merge_sort.py is similar to quick_sort.py in that it uses a recursive approach to sorting.
# The difference is that merge_sort.py uses a divide-and-conquer approach to sorting.
# The merge_sort.py snippet is shown below:
# # merge_sort.py

class merge_sort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        if len(self.arr) <= 1:
            return self.arr
        else:
            mid = len(self.arr) // 2
            left = merge_sort(self.arr[:mid]).sort()
            right = merge_sort(self.arr[mid:]).sort()
            return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    
print(merge_sort([5, 3, 8, 6, 7, 2]).sort())