package dp;

import java.util.Stack;

public class StackWithMax<T extends Comparable<T>> extends Stack<T> {

	private static final long serialVersionUID = 1L;
	
	private Stack<T> maxStack = new Stack<T>();
	
	public T push(T element) {
		if (maxStack.isEmpty()) {
			maxStack.push(element);
		} else if (element.compareTo(maxStack.peek()) >= 0) {
			maxStack.push(element);
		}
		return super.push(element);
	}
	
	public T pop() {
		T element = super.pop();
		if (element.equals(maxStack.peek())) {
			maxStack.pop();
		}
		return element;
	}
	
	public T max() {
		return maxStack.peek();
	}
	
	public static void main(String[] args) {
		StackWithMax<Integer> stack = new StackWithMax<>();
		stack.push(10);
		stack.push(5);
		System.out.println(stack.max());
		stack.push(15);
		System.out.println(stack.max());
		stack.pop();
		System.out.println(stack.max());
		stack.pop();
		System.out.println(stack.max());
	}
}
