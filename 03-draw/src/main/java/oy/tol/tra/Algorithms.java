package oy.tol.tra;


import java.util.function.Predicate;

public class Algorithms {

    public static <T> void reverse(T[] array) {
        int i = 0;
        while (i < array.length / 2) {
            swap(array, i, array.length - i - 1);
            i++;
        }
    }

    public static class ModeSearchResult<T> {
        public T theMode = null;
        public int count = -1;
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


    public static <T extends Comparable<T>> ModeSearchResult<T> findMode(T [] array) {
        ModeSearchResult<T> result = new ModeSearchResult<>();
        if (array == null || array.length < 2) return result;
        sort(array);

        int lcount = 1;
        T currentValue = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i].equals(currentValue)) {
                lcount++;
            } else {
                if (lcount > result.count) {
                    result.count = lcount;
                    result.theMode = currentValue;
                }
                lcount = 1;
                currentValue = array[i];
            }
        }
        if (lcount > result.count) {
            result.count = lcount;
            result.theMode = currentValue;
        }

        return result;
    }


    public static <T> int partitionByRule(T [] array, int count, Predicate<T> rule) {
        int index = 0;
        while (index < count && !rule.test(array[index])){
            index++;
        }
        if (index >= count) {
            return count;
        }

        int nextIndex = index + 1;
        while (nextIndex < count) {
            if (!rule.test(array[nextIndex])) {
                swap(array, index, nextIndex);
                index++;
            }
            nextIndex++;
        }
        return index;
    }

}