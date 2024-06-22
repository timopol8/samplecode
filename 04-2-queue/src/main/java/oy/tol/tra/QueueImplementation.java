package oy.tol.tra;

import java.util.Queue;

public class QueueImplementation<E> implements QueueInterface<E> {

    private Object[] itemArray;
    private int capacity;
    private static final int MY_DEFAULT_CAPACITY = 10;
    private int head = 0;
    private int tail = 0;


    public QueueImplementation() throws QueueAllocationException {
        this(MY_DEFAULT_CAPACITY);
    }
    public QueueImplementation(int capacity)  throws QueueAllocationException{
        if (capacity < 2) {
            throw new QueueAllocationException("capacity < 2");
        }
        this.capacity = capacity;
        try{
            itemArray = new Object[capacity];
        }
        catch (Exception e){
            throw new QueueAllocationException("Error allocating queue array");
        }
    }

    /**
     * For querying the current capacity of the queue.
     @return The number of elements the queue can currently hold.
     */
    @Override
    public int capacity() {
        return capacity;
    }

    /**
     * Add an element to the queue.
     * @param element The element to add, must not be null.
     * @throws QueueAllocationException If the reallocation for the queue failed in case queue needs reallocation.
     * @throws NullPointerException If the element is null.
     */
    @Override
    public void enqueue(E element) throws QueueAllocationException, NullPointerException{
        if (element == null){
            throw new NullPointerException("null element");
        }
        if (tail == capacity) {
            try {
                capacity = capacity * 2;
                Object[] newItemArray = new Object[capacity];
                for (int i =0; i<tail; i++) {
                    newItemArray[i] = itemArray[i];
                }
                itemArray = newItemArray;
            } catch (Exception e) {
                throw new QueueAllocationException("Failed to allocate new array");
            }
        }
        itemArray[tail] = element;
        tail++;
    }


    /**
     * Removes an element from the queue.
     * @return The element from the head of the queue.
     * @throws QueueIsEmptyException If the queue is empty.
     */
    @Override
    public E dequeue() throws QueueIsEmptyException{
        if (isEmpty()){
            throw new QueueIsEmptyException("Queue is empty");
        }
        head++;
        return (E) itemArray[head-1];
    }

    /**
     * Returns the element at the head of the queue, not removing it from the queue.
     * @return The element in the head of the queue.
     * @throws QueueIsEmptyException If the queue is empty.
     */
    @Override
    public E element() throws QueueIsEmptyException{
        if (isEmpty()){
            throw new QueueIsEmptyException("Queue is empty");
        }
        return (E) itemArray[head];
    }

    /**
     * Returns the count of elements currently in the queue.
     * @return Count of elements in the queue.
     */
    @Override
    public int size(){
        return(tail-head);
    }

    /**
     * Can be used to check if the queue is empty.
     * @return True if the queue is empty, false otherwise.
     */
    @Override
    public boolean isEmpty(){
        return (head==tail);
    }

    /**
     * Resets the queue to empty state, removing the objects.
     * There is no need to change the capacity, just keep it as it is.
     */
    @Override
    public void clear(){
        head =0;
        tail = 0;
    }

    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder("[");
        for (int i = head; i < tail; i++) {
            sb.append(itemArray[i]);
            if (i != tail - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }

}