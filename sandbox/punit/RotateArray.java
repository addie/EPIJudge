package dp;

import java.util.Arrays;

public class RotateArray {

	private void rotate(int[] array, int amount) {

		for (int j = 0; j < amount; j++) {
			int copy = array[0];
			int saved = -1;
			for (int i = 1; i < array.length; i++) {
				saved = array[i];
				array[i] = copy;
				copy = saved;
			}
			array[0] = copy;
		}

		System.out.println(Arrays.toString(array));
	}

	public static void main(String[] args) {
		int[] array = new int[] { 0, 1, 2, 3, 4, 5, 6 };
		new RotateArray().rotate(array, 3);
	}

}
