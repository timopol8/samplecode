package oy.tol.tra;

/**
 * An implementation of the StackInterface.
 * Note that you need to implement construtor(s) for your concrete StackImplementation, which
 * allocates the internal Object array for the Stack:
 * - a default constructor, calling the StackImplementation(int size) with value of 10.
 * - StackImplementation(int size), which allocates an array of Object's with size.
 *  -- remember to maintain the capacity and/or currentIndex when the stack is manipulated.
 */
public class StackImplementation<E> implements StackInterface<E> {

   private static final int MY_DEFAULT_CAPACITY = 10;
   private Object [] itemArray;

   private int capacity;
   private int currentIndex = 0;


   public StackImplementation() throws StackAllocationException {
      this(MY_DEFAULT_CAPACITY);
   }

   public StackImplementation(int capacity) throws StackAllocationException {
      if (capacity < 2) {
         throw new StackAllocationException("capacity < 2");
      }
      this.capacity = capacity;
      try {
         itemArray = new Object[capacity];
      }
      catch (Exception e){
         throw new StackAllocationException("Error allocating stack array");
      }
   }

   @Override
   public int capacity() {
      return capacity;
   }

   @Override
   public void push(E element) throws StackAllocationException, NullPointerException {
      if (element==null) {
         throw new NullPointerException("null element");
      }
      if (currentIndex == capacity) {
         try {
            capacity = capacity * 2;
            Object[] newItemArray = new Object[capacity];
            for (int i =0; i<currentIndex; i++) {
               newItemArray[i] = itemArray[i];
            }
            itemArray = newItemArray;
         } catch (Exception e) {
            throw new StackAllocationException("Failed to allocate new array");
         }
      }
      itemArray[currentIndex++] = element;
   }

   @SuppressWarnings("unchecked")
   @Override
   public E pop() throws StackIsEmptyException {
      if (currentIndex == 0) {
         throw new StackIsEmptyException("");
      }
      currentIndex--;
      return (E) itemArray[currentIndex];
   }

   @SuppressWarnings("unchecked")
   @Override
   public E peek() throws StackIsEmptyException {
      if (currentIndex == 0) {
         throw new StackIsEmptyException("");
      }
      return (E) itemArray[currentIndex - 1];
   }

   @Override
   public int size() {
      return currentIndex;
   }

   @Override
   public void clear() {
      currentIndex = 0;
   }

   @Override
   public boolean isEmpty() {
      return currentIndex==0;
   }

   @Override
   public String toString() {
      StringBuilder sb = new StringBuilder("[");
      for (int i = 0; i < currentIndex; i++) {
         sb.append(itemArray[i]);
         if (i != currentIndex - 1) {
            sb.append(", ");
         }
      }
      sb.append("]");
      return sb.toString();
   }
}
