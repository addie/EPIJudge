package dp;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

public class QueueWithMax<T extends Comparable<T>> extends LinkedList<T> {

	private static final long serialVersionUID = 1L;

	private Deque<T> dequeue = new ArrayDeque<>();

	public boolean add(T element) {
		while (!dequeue.isEmpty() && element.compareTo(dequeue.peekLast()) >= 0) {
			dequeue.removeLast();
		}
		dequeue.addLast(element);

		return super.add(element);
	}

	public T remove() {
		T element = super.remove();
		if (element.equals(dequeue.peekFirst())) {
			dequeue.removeFirst();
		}
		return element;
	}

	public T max() {
		return dequeue.peekFirst();
	}

	public static void main(String[] args) {
		QueueWithMax<Integer> queue = new QueueWithMax<>();
		queue.add(10);
		queue.add(5);
		System.out.println(queue.max());
		queue.add(15);		
		queue.add(7);
		System.out.println(queue.max());
		queue.remove();
		System.out.println(queue.max());
		queue.remove();
		System.out.println(queue.max());
		queue.remove();
		System.out.println(queue.max());
	}
}
