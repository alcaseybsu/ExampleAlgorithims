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

## Searching Algorithms

### Binary Search
Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you have narrowed down the possible locations to just one.

#### Algorithm Explanation
Binary Search works as follows:
1. Start with the middle element of the sorted array.
2. If the middle element is equal to the target element, the search is complete.
3. If the target element is less than the middle element, repeat the search with the left half of the array.
4. If the target element is greater than the middle element, repeat the search with the right half of the array.
5. Continue the process until the target element is found or the subarray size becomes zero.

#### Running Time
- **Best Case:** The best-case time complexity is \(O(1)\), which occurs when the target element is the middle element of the array.
- **Average Case:** The average-case time complexity is \(O(\log n)\). This is because the array is divided in half during each step of the search.
- **Worst Case:** The worst-case time complexity is also \(O(\log n)\), which occurs when the search continues until the smallest subarray size is reached.

- **Space Complexity:** The space complexity of Binary Search is \(O(1)\) for the iterative version and \(O(\log n)\) for the recursive version due to the call stack.

---

### Linear Search
Linear Search is a simple searching algorithm that checks each element in the list sequentially until the desired element is found or the list ends. It is the most straightforward search algorithm.

#### Algorithm Explanation
Linear Search works as follows:
1. Start from the first element of the array.
2. Compare the current element with the target element.
3. If the current element is equal to the target element, the search is complete.
4. If the current element is not equal to the target element, move to the next element and repeat step 2.
5. Continue this process until the target element is found or the end of the array is reached.

#### Running Time
- **Best Case:** The best-case time complexity is \(O(1)\), which occurs when the target element is the first element of the array.
- **Average Case:** The average-case time complexity is \(O(n)\). This occurs because, on average, the target element might be located in the middle of the array.
- **Worst Case:** The worst-case time complexity is also \(O(n)\). This occurs when the target element is the last element of the array or not present in the array.

- **Space Complexity:** The space complexity of Linear Search is \(O(1)\) as it requires a constant amount of additional memory space for variables.

---  

## Graph Algorithms

### Dijkstra's Algorithm
Dijkstra's Algorithm is a shortest-path algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. The algorithm works on both directed and undirected graphs with non-negative weights.

#### Algorithm Explanation
Dijkstra's Algorithm works as follows:
1. Initialize the distance to the starting node to 0 and the distance to all other nodes to infinity.
2. Set the starting node as the current node.
3. For the current node, consider all its neighbors and calculate their tentative distances through the current node.
4. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.
5. Once all neighbors of the current node have been considered, mark the current node as visited.
6. Select the unvisited node with the smallest tentative distance as the new current node and repeat steps 3-5.
7. The algorithm continues until all nodes have been visited or the smallest tentative distance among the unvisited nodes is infinity.

#### Running Time
- **Best Case:** The best-case time complexity is \(O(E + V \log V)\) using a priority queue and adjacency list, where \(V\) is the number of vertices and \(E\) is the number of edges.
- **Average Case:** The average-case time complexity is also \(O(E + V \log V)\) under the same conditions.
- **Worst Case:** The worst-case time complexity is \(O(E + V \log V)\), making it efficient for sparse graphs with a relatively low number of edges compared to vertices.

- **Space Complexity:** The space complexity of Dijkstra's Algorithm is \(O(V + E)\) due to the storage required for the graph representation and priority queue.

---

### Breadth-First Search (BFS)
Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root (or an arbitrary node in the case of a graph) and explores all neighbors at the present depth prior to moving on to nodes at the next depth level.

#### Algorithm Explanation
Breadth-First Search works as follows:
1. Initialize a queue and enqueue the starting node.
2. Mark the starting node as visited.
3. While the queue is not empty:
   - Dequeue the front node from the queue.
   - For the current node, consider all its unvisited neighbors, mark them as visited, and enqueue them.
4. Repeat step 3 until the queue is empty.

#### Running Time
- **Best Case:** The best-case time complexity is \(O(V + E)\), where \(V\) is the number of vertices and \(E\) is the number of edges. This is because each vertex and each edge will be explored in the worst case.
- **Average Case:** The average-case time complexity is also \(O(V + E)\) for the same reasons.
- **Worst Case:** The worst-case time complexity is \(O(V + E)\), as BFS explores every vertex and edge.

- **Space Complexity:** The space complexity of Breadth-First Search is \(O(V)\), due to the space required to store the queue and the visited nodes.

---  

