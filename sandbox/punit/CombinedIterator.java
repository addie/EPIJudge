package dp;

import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class CombinedIterator<T> implements Iterator<T> {

	private Iterator<? extends T> currentIterator;
	private Iterator<? extends T> removeIterator;
	private final Iterator<? extends Iterator<? extends T>> baseIterator;

	public CombinedIterator(Iterator<? extends Iterator<? extends T>> iterators) {
		this.baseIterator = iterators;
		currentIterator = Collections.emptyIterator();
	}

	@Override
	public boolean hasNext() {
		if (currentIterator.hasNext()) {
			return true;
		} else {
			while (baseIterator.hasNext()) {
				currentIterator = baseIterator.next();
				if (currentIterator != null && currentIterator.hasNext()) {
					return true;
				}
			}
		}
		return false;
	}

	@Override
	public T next() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		removeIterator = currentIterator;
		return currentIterator.next();
	}

	@Override
	public void remove() {
		removeIterator.remove();
		removeIterator = null;
	}

	public static void main(String[] args) {
		List<Integer> list1 = Arrays.asList(1, 2, 3);
		List<Integer> list2 = Arrays.asList(4, 5);
		List<Integer> list3 = Arrays.asList(6);
		CombinedIterator<Integer> ci = new CombinedIterator<Integer>(
				Arrays.asList(list1.iterator(), list2.iterator(), list3.iterator()).iterator());
		while (ci.hasNext()) {
			System.out.println(ci.next());
		}
	}
}
