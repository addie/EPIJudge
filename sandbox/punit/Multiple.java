package dp;

import java.util.PriorityQueue;

public class Multiple {
	
	public static class Pair implements Comparable<Pair> {
		
		public final int x;
		public final int y;
		
		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}

		public int compareTo(Pair o) {
			return x - o.x;
		}
	};
	
	public static void nthMultiple(int[] array, int n) {
		PriorityQueue<Pair> heap = new PriorityQueue<Pair>(array.length);
		for (int i = 0; i < array.length; i++) {
			heap.add(new Pair(array[i], i));
		}
		
		Pair top = null;
		while (n > 0) {
			top = heap.poll();
			heap.add(new Pair(top.x + array[top.y], top.y));
			while (top.x == heap.peek().x) {
				// removes duplicates from consideration in terms of n
				// but need to add these multiples in for later use
				Pair temp = heap.poll();
				heap.add(new Pair(temp.x + array[temp.y], temp.y));
			}			
			n--;
			
			//System.out.println("n " + n + " top " + top.x);
		}
		System.out.println(top.x);
	}

	public static void main(String[] args) {
		Multiple.nthMultiple(new int[] {5, 7}, 4);
		Multiple.nthMultiple(new int[] {5, 7}, 5);
		Multiple.nthMultiple(new int[] {2, 3}, 4);
		Multiple.nthMultiple(new int[] {2, 3}, 5);
		Multiple.nthMultiple(new int[] {2, 3}, 6);
		Multiple.nthMultiple(new int[] {2, 3}, 7);
		Multiple.nthMultiple(new int[] {2, 3}, 8);
		Multiple.nthMultiple(new int[] {2, 3}, 9);
		Multiple.nthMultiple(new int[] {2, 3, 4, 5, 6, 7, 8, 9}, 50);
	}

}
