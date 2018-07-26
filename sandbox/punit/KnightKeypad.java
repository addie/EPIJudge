package dp;

import java.util.ArrayList;
import java.util.List;

public class KnightKeypad {

	private int recurseCounter = 0;
	private int iterationCounter = 0;
	
	int[] row = new int[] { -2, -2, -1, -1, 2, 2, 1, 1 };
	int[] col = new int[] { 1, -1, 2, -2, 1, -1, 2, -2 };

	private void getPhoneNumbers(char keypad[][], String currentNumber, int i, int j, int n, List<String> all) {

		recurseCounter++;

		currentNumber += keypad[i][j];
		if (n == 9) {
			assert currentNumber.length() == 10;
			all.add(currentNumber.toString());
			return;
		}
		
		for (int m = 0; m < row.length; m++) {
			int r = i + row[m];
			int c = j + col[m];

			if (r >= 0 && r <= 3 && c >= 0 && c <= 2 && keypad[r][c] != '*' && keypad[r][c] != '#') {
				getPhoneNumbers(keypad, currentNumber, r, c, n + 1, all);
			}
		}

		/*
		 * getPhoneNumbers(keypad, currentNumber,i - 2, j + 1, n + 1, all);
		 * getPhoneNumbers(keypad, currentNumber,i - 2, j - 1, n + 1, all);
		 * getPhoneNumbers(keypad, currentNumber,i - 1, j + 2, n + 1, all);
		 * getPhoneNumbers(keypad, currentNumber,i - 1, j - 2, n + 1, all);
		 * getPhoneNumbers(keypad, currentNumber,i + 2, j + 1, n + 1, all);
		 * getPhoneNumbers(keypad, currentNumber,i + 2, j - 1, n + 1, all);
		 * getPhoneNumbers(keypad, currentNumber,i + 1, j + 2, n + 1, all);
		 * getPhoneNumbers(keypad, currentNumber,i + 1, j - 2, n + 1, all);
		 */
	}

	// Returns count of numbers of length n starting from key position
	// (i, j) in a numeric keyboard.
	private int getCountUtil(char keypad[][], int i, int j, int n) {
		if (keypad == null || n <= 0)
			return 0;

		if (!(i >= 0 && i <= 3 && j >= 0 && j <= 2 && keypad[i][j] != '*' && keypad[i][j] != '#')) {
			return 0;
		}

		recurseCounter++;

		// From a given key, only one number is possible of length 1
		if (n == 1)
			return 1;

		int totalCount = 0;

		// figure out possible moves
		totalCount += getCountUtil(keypad, i - 2, j + 1, n - 1);
		totalCount += getCountUtil(keypad, i - 2, j - 1, n - 1);
		totalCount += getCountUtil(keypad, i - 1, j + 2, n - 1);
		totalCount += getCountUtil(keypad, i - 1, j - 2, n - 1);
		totalCount += getCountUtil(keypad, i + 2, j + 1, n - 1);
		totalCount += getCountUtil(keypad, i + 2, j - 1, n - 1);
		totalCount += getCountUtil(keypad, i + 1, j + 2, n - 1);
		totalCount += getCountUtil(keypad, i + 1, j - 2, n - 1);

		return totalCount;
	}

	private int getCount(char keypad[][], int n) {
		// Base cases
		if (keypad == null || n <= 0)
			return 0;
		if (n == 1)
			return 10;

		int i = 0, j = 0, totalCount = 0;
		for (i = 0; i < 4; i++) // Loop on keypad row
		{
			for (j = 0; j < 3; j++) // Loop on keypad column
			{
				// Process for 0 to 9 digits
				if (keypad[i][j] != '*' && keypad[i][j] != '#') {
					// Get count when number is starting from key
					// position (i, j) and add in count obtained so far
					int count = getCountUtil(keypad, i, j, n);
					totalCount += count;
					System.out.println("Count for " + i + "," + j + " is " + count);
				}
			}
		}
		return totalCount;
	}

	private int getCountDP(char keypad[][]) {
		int n = 10;

		// taking n+1 for simplicity - count[i][j] will store
		// number count starting with digit i and length j
		int count[][] = new int[10][n + 1];
		int i = 0, j = 0, k = 0, num = 0, totalCount = 0;

		// count numbers starting with digit i and of lengths 0 and 1
		for (i = 0; i <= 9; i++) {
			count[i][0] = 0;
			count[i][1] = 1;
		}

		// Bottom up - Get number count of length 2, 3, 4, ... , n
		for (k = 2; k <= n; k++) {
			for (i = 0; i < 4; i++) // Loop on keypad row
			{
				for (j = 0; j < 3; j++) // Loop on keypad column
				{
					if (keypad[i][j] != '*' && keypad[i][j] != '#') {
						// Here we are counting the numbers starting with
						// digit keypad[i][j] and of length k keypad[i][j]
						// will become 1st digit, and we need to look for
						// (k-1) more digits
						num = keypad[i][j] - '0';
						count[num][k] = 0;

						iterationCounter++;

						count[num][k] += getCountDP(keypad, i - 2, j + 1, k, count);
						count[num][k] += getCountDP(keypad, i - 2, j - 1, k, count);
						count[num][k] += getCountDP(keypad, i - 1, j + 2, k, count);
						count[num][k] += getCountDP(keypad, i - 1, j - 2, k, count);
						count[num][k] += getCountDP(keypad, i + 2, j + 1, k, count);
						count[num][k] += getCountDP(keypad, i + 2, j - 1, k, count);
						count[num][k] += getCountDP(keypad, i + 1, j + 2, k, count);
						count[num][k] += getCountDP(keypad, i + 1, j - 2, k, count);
					}
				}
			}
		}

		// Get count of all possible numbers of length "n" starting
		// with digit 0, 1, 2, ..., 9
		totalCount = 0;
		for (i = 0; i <= 9; i++) {
			System.out.println("DP count for " + i + " is " + count[i][n]);
			totalCount += count[i][n];
		}
		return totalCount;
	}

	private int getCountDP(char keypad[][], int i, int j, int k, int count[][]) {

		if (i >= 0 && i <= 3 && j >= 0 && j <= 2 && keypad[i][j] != '*' && keypad[i][j] != '#') {
			int nextNum = keypad[i][j] - '0';
			return count[nextNum][k - 1];
		} else {
			return 0;
		}
	}

	public static void main(String[] args) {
		char keypad[][] = { { '1', '2', '3' }, { '4', '5', '6' }, { '7', '8', '9' }, { '*', '0', '#' } };

		KnightKeypad pad = new KnightKeypad();
		System.out.println("Total count is " + pad.getCount(keypad, 10));
		System.out.println("Recursions is " + pad.recurseCounter);

		System.out.println("Total DP count is " + pad.getCountDP(keypad));
		System.out.println("Iterations is " + pad.iterationCounter);

		pad.recurseCounter = 0;
		List<String> nums = new ArrayList<String>();
		pad.getPhoneNumbers(keypad, new String(), 0, 0, 0, nums);
		System.out.println("Phone number count is " + nums.size());
		System.out.println("Recursions is " + pad.recurseCounter);
	}
}
