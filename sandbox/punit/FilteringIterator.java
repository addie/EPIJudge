package dp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class FilteringIterator<E> implements Iterator<E> {

	public interface Predicate<E> {
		boolean matches(E value);
	};
	
	private final Iterator<E> base;
	private final Predicate<E> predicate;
	private E next;
	private Boolean hasNext;
	private boolean movedNext = false;
	
	public FilteringIterator(Iterator<E> base, Predicate<E> predicate) {
		this.base = base;
		this.predicate = predicate;		
	}
	
	@Override
	public boolean hasNext() {
		if (hasNext != null) {
			return hasNext;
		}
		
		hasNext = false;
		while (base.hasNext()) {
			next = base.next();
			if (predicate.matches(next)) {
				hasNext = true;
				break;
			}
		}
		
		return hasNext;
	}

	@Override
	public E next() {
		if (!hasNext()) {
			throw new NoSuchElementException();
		}
		
		E retval = next;
		next = null;
		hasNext = null;
		movedNext = true;
		return retval;
	}

	@Override
	public void remove() {
		if (movedNext) {
			movedNext = false;
			base.remove();
		} else {
			throw new IllegalStateException();
		}		
	}
	
	public static void main(String[] args) {
		List<Integer> list1 = Arrays.asList(null, null, 10, null, 5, null, 2,3, null,null,20,null,null,1);
		List<Integer> list = new ArrayList<>(list1);
		FilteringIterator<Integer> filterIter = new FilteringIterator<Integer>(list.iterator(), new Predicate<Integer>() {

			@Override
			public boolean matches(Integer value) {
				//return value != null && value % 5 == 0;
				return value == null;
			}
			
		});
		while (filterIter.hasNext()) {
			System.out.println(filterIter.next());
			filterIter.remove();
		}
		
		for (Integer l : list) {
			System.out.println(l);
		}
	}

}
