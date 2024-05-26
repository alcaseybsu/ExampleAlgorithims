package algorithms.Java.Sorting;

// Merge sort is a divide-and-conquer algorithm that divides an array into two halves, sorts each half, and then merges the sorted halves to produce a sorted array. 

public class MergeSort {

  public static void mergeSort(int[] arr, int left, int right) {
    if (left < right) {
      int middle = (left + right) / 2;
      mergeSort(arr, left, middle);
      mergeSort(arr, middle + 1, right);
      merge(arr, left, middle, right);
    }
  }

  private static void merge(int[] arr, int left, int middle, int right) {
    int n1 = middle - left + 1;
    int n2 = right - middle;

    int[] L = new int[n1];
    int[] R = new int[n2];

    System.arraycopy(arr, left, L, 0, n1);
    System.arraycopy(arr, middle + 1, R, 0, n2);

    int i = 0, j = 0;
    int k = left;
    while (i < n1 && j < n2) {
      if (L[i] <= R[j]) {
        arr[k] = L[i];
        i++;
      } else {
        arr[k] = R[j];
        j++;
      }
      k++;
    }

    while (i < n1) {
      arr[k] = L[i];
      i++;
      k++;
    }

    while (j < n2) {
      arr[k] = R[j];
      j++;
      k++;
    }
  }

  public static void main(String[] args) {
    int[] arr = { 12, 11, 13, 5, 6, 7 };
    mergeSort(arr, 0, arr.length - 1);
    System.out.println("Sorted array:");
    for (int i : arr) {
      System.out.print(i + " ");
    }
  }
}
