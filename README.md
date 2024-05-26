# Algorithm Examples

This repository contains implementations of various algorithms in Java, Python, and C#. These examples are provided to demonstrate proficiency in algorithm design and analysis, and to serve as a reference guide.

## Table of Contents
- [Sorting Algorithms](#sorting-algorithms)
  - [Bubble Sort](#bubble-sort)
  - [Quick Sort](#quick-sort)
  - [Merge Sort](#merge-sort)
  - [Insertion Sort](#insertion-sort)
  - [Heap Sort](#heap-sort)
- [Searching Algorithms](#searching-algorithms)
  - [Binary Search](#binary-search)
  - [Linear Search](#linear-search)
- [Graph Algorithms](#graph-algorithms)
  - [Dijkstra's Algorithm](#dijkstras-algorithm)
  - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
- [Dynamic Programming](#dynamic-programming)
  - [Fibonacci](#fibonacci)
  - [Knapsack](#knapsack)

---  

## Sorting Algorithms

### Bubble Sort
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

#### Algorithm Explanation
Bubble Sort works as follows:
1. Compare the first two elements. If the first is greater than the second, swap them.
2. Move to the next pair of elements and repeat the comparison and swap if necessary.
3. Continue this process for each pair of adjacent elements to the end of the list.
4. Repeat the entire process until no swaps are needed, indicating that the list is sorted.

#### Running Time
- **Best Case:** The best-case time complexity is \(O(n)\), which occurs when the array is already sorted. In this case, the algorithm only needs to make one pass through the array to confirm that it is sorted.
- **Average Case:** The average-case time complexity is \(O(n^2)\). This occurs when the elements are in random order.
- **Worst Case:** The worst-case time complexity is also \(O(n^2)\). This occurs when the array is sorted in reverse order.

- **Space Complexity:** The space complexity of Bubble Sort is \(O(1)\), as it only requires a constant amount of additional memory space for variables.

---  

### Quick Sort
Quick Sort is an efficient, comparison-based sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

#### Algorithm Explanation
Quick Sort works as follows:
1. Pick a pivot element from the array. Common choices include:
   - The first element.
   - The last element.
   - A random element.
   - The median.
2. Partition the array into two sub-arrays:
   - Elements less than the pivot.
   - Elements greater than the pivot.
3. Recursively apply the above steps to the sub-arrays.
4. Combine the sub-arrays and the pivot to get the sorted array.

#### Running Time
- **Best Case:** The best-case time complexity is \(O(n \log n)\), which occurs when the pivot element divides the array into two equal halves at each step.
- **Average Case:** The average-case time complexity is \(O(n \log n)\). This is because, on average, the pivot will divide the array into reasonably balanced partitions.
- **Worst Case:** The worst-case time complexity is \(O(n^2)\), which occurs when the pivot selection results in highly unbalanced partitions, such as when the array is already sorted, and the first or last element is always chosen as the pivot.

- **Space Complexity:** The space complexity of Quick Sort is \(O(\log n)\) due to the recursive call stack.

---  

### Merge Sort
Merge Sort is an efficient, stable, and comparison-based sorting algorithm. It divides the input array into two halves, recursively sorts each half, and then merges the two sorted halves to produce the final sorted array.

#### Algorithm Explanation
Merge Sort works as follows:
1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves into a single sorted array.

#### Running Time
- **Best Case:** The best-case time complexity is \(O(n \log n)\). This occurs because the array is always divided into halves, and the merging process takes linear time.
- **Average Case:** The average-case time complexity is \(O(n \log n)\). This is due to the divide-and-conquer approach, which ensures that the time complexity remains consistent.
- **Worst Case:** The worst-case time complexity is also \(O(n \log n)\). This occurs regardless of the initial order of the elements, as the process of division and merging remains the same.

- **Space Complexity:** The space complexity of Merge Sort is \(O(n)\), as it requires additional space to store the divided halves and the merged array.

---  

### Insertion Sort
Insertion Sort is a simple and intuitive comparison-based sorting algorithm. It builds the final sorted array one element at a time, with the array being divided into a sorted and an unsorted region. Values from the unsorted region are picked and placed in their correct position in the sorted region.

#### Algorithm Explanation
Insertion Sort works as follows:
1. Start with the first element, assuming it is sorted.
2. Pick the next element and compare it with the elements in the sorted region.
3. Shift all elements in the sorted region that are greater than the picked element to the right.
4. Insert the picked element at the correct position.
5. Repeat steps 2-4 for all remaining elements in the unsorted region.

#### Running Time
- **Best Case:** The best-case time complexity is \(O(n)\), which occurs when the array is already sorted. In this case, each element is compared once with its predecessor.
- **Average Case:** The average-case time complexity is \(O(n^2)\). This is because, on average, each insertion takes half the size of the array steps.
- **Worst Case:** The worst-case time complexity is also \(O(n^2)\). This occurs when the array is sorted in reverse order, requiring each element to be compared with all previously sorted elements.

- **Space Complexity:** The space complexity of Insertion Sort is \(O(1)\), as it only requires a constant amount of additional memory space for variables.

---  

### Heap Sort
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It is similar to selection sort, but it uses a heap to find the maximum or minimum element more efficiently.

#### Algorithm Explanation
Heap Sort works as follows:
1. Build a max heap from the input data. A max heap is a complete binary tree where the value of each node is greater than or equal to the values of its children.
2. The largest item is stored at the root of the heap. Swap it with the last item of the heap and then reduce the size of the heap by one. 
3. Heapify the root of the tree to ensure the heap property is maintained.
4. Repeat steps 2 and 3 until the heap size is reduced to one.

#### Running Time
- **Best Case:** The best-case time complexity is \(O(n \log n)\), which occurs because the heap operations (building the heap and heapify) are \(O(\log n)\) and there are \(n\) such operations.
- **Average Case:** The average-case time complexity is \(O(n \log n)\). This is because the process of building the heap and performing the sort takes \(O(n \log n)\) time.
- **Worst Case:** The worst-case time complexity is also \(O(n \log n)\). This occurs regardless of the initial order of the elements, as the process of heapifying maintains the same complexity.

- **Space Complexity:** The space complexity of Heap Sort is \(O(1)\), as it is an in-place sorting algorithm that only requires a constant amount of additional memory space.

---  

