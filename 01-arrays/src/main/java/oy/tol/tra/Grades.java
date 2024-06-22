package oy.tol.tra;

import java.lang.Comparable;

/**
 * A simple array of student grades to be used in testing
 * misbehaving algorithm for reversing the array.
 */
public class Grades {
   
   private Integer [] grades = null;

   /**
    * A constructor for building IntArrays.
    * @param grades the plain Java integer array with numbers to add.
    */
   public Grades(Integer [] grades) {
      this.grades = new Integer [grades.length];
      for (int counter = 0; counter < grades.length; counter++) {
         this.grades[counter] = grades[counter];
      }
   }

   public void reverse() {

      int i = 0;
      while (i < grades.length/2) {
         int temp = grades[i];
         grades[i] = grades[grades.length-i-1];
         grades[grades.length-i-1] = temp;
         i++;
      }
   }

   /**
    * Sorts the array to ascending order.
    */
   public void sort() {
      int l = grades.length;
      boolean swapped = true;
      while (swapped) {
         swapped = false;
         for (int i = 1; i < l; i++) {
            if (grades[i] < grades[i - 1]) {
               int tmp = grades[i];
               grades[i] = grades[i - 1];
               grades[i - 1] = tmp;
               swapped = true;
            }
         }
         l--;
      }
   }


   public Integer [] getArray() {
      return grades;
   }
}

