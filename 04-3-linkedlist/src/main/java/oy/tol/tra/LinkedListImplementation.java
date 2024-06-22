package oy.tol.tra;

public class LinkedListImplementation<E> implements LinkedListInterface<E> {

   private class Node<T> {
      Node(T data) {
         element = data;
         next = null;
      }

      T element;
      Node<T> next;

      @Override
      public String toString() {
         return element.toString();
      }
   }

   private Node<E> head = null;
   private int size = 0;


   @Override
   public void add(E element) throws NullPointerException, LinkedListAllocationException {

      if (element == null) {
         throw new NullPointerException("element is null");
      }

      Node<E> addedNode;
      try {
         addedNode = new Node<E>(element);
      } catch (Exception e) {
         throw new LinkedListAllocationException("Failed to allocate a new list element");
      }

      if (head == null) {                // The list is empty, so the new node becomes the head.
         head = addedNode;
      } else {                           // Traverse the list to find the last node and append the new node.
         Node<E> current = head;
         while (current.next != null) {
            current = current.next;
         }
         current.next = addedNode;
      }
      size++;
   }


   @Override
   public void add(int index, E element) throws NullPointerException, LinkedListAllocationException, IndexOutOfBoundsException {
      if (element == null) {
         throw new NullPointerException("element is null");
      }
      if (!(index >= 0 && index <= size())) {
         throw new IndexOutOfBoundsException("index is out of bounds");
      }

      Node<E> addedNode;
      try {
         addedNode = new Node<E>(element);
      } catch (Exception e) {
         throw new LinkedListAllocationException("Failed to allocate a new list element");
      }

      if (index == 0) {
         addedNode.next = head;
         head = addedNode;
      }
      // Traverse the list to find the target node and append the new node.
      else {
         Node<E> target = head;
         for (int i = 0; i < index - 1; i++) {
            target = target.next;
         }
         addedNode.next = target.next;
         target.next = addedNode;
      }
      size++;
   }

   @Override
   public boolean remove(E element) throws NullPointerException {
      if (element == null) {
         throw new NullPointerException("parameter element is null");
      }
      //if the list is empty
      if (head == null) {
         return false;
      }
      //if element == head.element
      if (head.element.equals(element)) {
         head = head.next;
         size--;
         return true;
      }
      //find the target
      Node<E> prev = head;
      Node<E> current = head.next;
      while (current != null && !current.element.equals(element)) {
         current = current.next;
         prev = prev.next;
      }
      //remove, return true
      if (current != null) {
         prev.next = current.next;
         size--;
         return true;
      }
      return false;
   }

   @Override
   public E remove(int index) throws IndexOutOfBoundsException {
      if (!(index >= 0 && index < size())) {
         throw new IndexOutOfBoundsException("index is out of bounds");
      }
      //if the list is empty
      if (head == null) {
         return null;
      }
      //if index == 0
      if (index == 0) {
         Node<E> ret = head;
         head = head.next;
         size--;
         return ret.element;
      }
      //find the target
      Node<E> target = head;
      for (int i = 0; i < index - 1; i++) {
         target = target.next;
      }

      Node<E> ret = target.next;
      target.next = target.next.next;
      size--;
      return ret.element;
   }

   @Override
   public E get(int index) throws IndexOutOfBoundsException {
      if (!(index >= 0 && index < size())) {
         throw new IndexOutOfBoundsException("index is out of bounds");
      }
      //if the list is empty
      if (head == null) {
         return null;
      }
      //if index == 0
      if (index == 0) {
         return head.element;
      }
      //find the target
      Node<E> target = head;
      for (int i = 0; i < index; i++) {
         target = target.next;
      }
      return target.element;
   }

   @Override
   public int indexOf(E element) throws NullPointerException {
      if (element == null) {
         throw new NullPointerException("parameter element is null");
      }

      //if the list is empty
      if (head == null) {
         return -1;
      }
      //if element == head.element
      if (head.element.equals(element)) {
         return 0;
      }

      //find the target
      Node<E> current = head;
      int index = 0;
      while (current != null && !current.element.equals(element)) {
         current = current.next;
         index++;
      }
      if (current != null) {
         return index;
      } else {
         return -1;
      }
   }

   @Override
   public int size() {
      return size;
   }

   @Override
   public void clear() {
      head = null;
      size = 0;
   }

   @Override
   public void reverse() {
      if (size<2) return;
      //  traverse the list and change the direction of the links.
      Node<E> target = head.next;
      head.next = null;
      Node<E> prev = head;
      while(!(target==null)) {
         Node<E> next = target.next;
         target.next=prev;
         prev=target;
         if (next==null){
            head = target;
         }
         target = next;
      }
   }

   @Override
   public String toString() {
      StringBuilder sb = new StringBuilder("[");
      Node<E> target = head;
      for (int i = 0; i < size; i++) {
         sb.append(target.element);
         if (i != size - 1) {
            sb.append(", ");
         }
         target = target.next;
      }
      sb.append("]");
      return sb.toString();
   }
}
