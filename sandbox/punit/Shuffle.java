package dp;

import java.util.Arrays;

public class Shuffle {

	private static void shuffle(int[] array) {

		for (int i = 0; i < array.length; i++) {
			int rand = i + (int) (Math.random() * (array.length - i));
			System.out.println("i " + i + " rand " + rand);
			int temp = array[i];
			array[i] = array[rand];
			array[rand] = temp;
		}
		
		System.out.println(Arrays.toString(array));

	}

	public static void main(String[] args) {
		shuffle(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 });
	}

}
