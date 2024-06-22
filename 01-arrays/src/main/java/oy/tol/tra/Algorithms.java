package oy.tol.tra;

public class Algorithms {

    public static <T> void reverse(T[] array) {
        int i = 0;
        while (i < array.length / 2) {
            swap(array, i, array.length - i - 1);
            i++;
        }
    }


    public static <T extends Comparable<T>> void sort(T[] array) {

        int l = array.length;
        boolean swapped = true;
        while (swapped) {
            swapped = false;
            for (int i = 1; i < l; i++) {
                if (array[i].compareTo(array[i - 1]) < 0) {
                    swap(array, i, i - 1);
                    swapped = true;
                }
            }
            l--;
        }
    }

    public static <T> void swap(T[] array, int num1, int num2) {
        T tmp = array[num1];
        array[num1] = array[num2];
        array[num2] = tmp;
    }
}