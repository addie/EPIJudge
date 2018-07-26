package dp;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class PeekIterator<T> implements Iterator<T> {

	private final Iterator<T> underlying;
	private T top;
	// keep separate flag b/c the underlying iterator could have null values so
	// don't use the "top = null" as a proxy for having checked if we peeked.
	private Boolean peeked;

	public PeekIterator(Iterator<T> underlying) {
		this.underlying = underlying;
	}

	public T peek() {
		if (peeked != null) {
			return top;
		} else {
			if (underlying.hasNext()) {
				top = underlying.next();
				peeked = true;
				return top;
			} else {
				top = null;
				peeked = false;
				return null;
			}
		}
	}

	@Override
	public boolean hasNext() {
		if (peeked != null) {
			return peeked;
		} else {
			return underlying.hasNext();
		}
	}

	@Override
	public T next() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}

		if (peeked != null) {
			T returnVal = top;
			top = null;
			peeked = null;
			return returnVal;
		} else {
			return underlying.next();
		}
	}

	@Override
	public void remove() {
		throw new UnsupportedOperationException();
	}

	public static void main(String[] args) {
		List<Integer> list = Arrays.asList(5, null, 1, 7);
		PeekIterator<Integer> peekIter = new PeekIterator<Integer>(list.iterator());
		System.out.println(peekIter.peek());
		System.out.println(peekIter.peek());
		System.out.println(peekIter.peek());
		System.out.println(peekIter.hasNext());
		System.out.println(peekIter.next());
		System.out.println(peekIter.peek());
		System.out.println(peekIter.peek());
		System.out.println(peekIter.hasNext());
		System.out.println(peekIter.next());
		System.out.println(peekIter.peek());
		System.out.println(peekIter.peek());
		System.out.println(peekIter.hasNext());
		System.out.println(peekIter.peek());
		System.out.println(peekIter.peek());
		System.out.println(peekIter.next());
		System.out.println(peekIter.hasNext());
		System.out.println(peekIter.peek());
	}

}
