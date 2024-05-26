package algorithms.Java.Sorting;

// Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.  

public class InsertionSort {

  public static void insertionSort(int[] arr) {
    int n = arr.length;
    for (int i = 1; i < n; i++) {
      int key = arr[i];
      int j = i - 1;
      while (j >= 0 && arr[j] > key) {
        arr[j + 1] = arr[j];
        j--;
      }
      arr[j + 1] = key;
    }
  }

  public static void main(String[] args) {
    int[] arr = { 12, 11, 13, 5, 6 };
    insertionSort(arr);
    System.out.println("Sorted array:");
    for (int i : arr) {
      System.out.print(i + " ");
    }
  }
}
