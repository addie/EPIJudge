package dp;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class GameOfLife {

	/**
	 * At each step of the simulation, cells with exactly one living neighbor
	 * change their status (alive cells become dead, dead cells become alive).
	 */
	private static void gameOfLife1D(int[] input) {
		int n = input.length;
		for (int i = 0; i < input.length; i++) {
			boolean leftAlive = (input[(i - 1 + n) % n] & 1) == 1;
			boolean rightAlive = (input[(i + 1 + n) % n] & 1) == 1;
			int totalAlive = (leftAlive ? 1 : 0) + (rightAlive ? 1 : 0);
			if (totalAlive == 1) { // flip status
				if (input[i] == 0) {
					input[i] = 2; // 1 0 (become alive)
				} // 1 stays as 0 1 (die)
			} else {
				if (input[i] == 1) { // keep existing status
					input[i] = 3; // 1 1 (stay alive)
				} else {
					input[i] = 0;
				}
			}
		}

		for (int i = 0; i < input.length; i++) {
			input[i] = input[i] >> 1;
		}

		System.out.println(Arrays.toString(input));
	}

	private static class Coord {
		int i;
		int j;

		private Coord(int i, int j) {
			this.i = i;
			this.j = j;
		}

		public boolean equals(Object o) {
			return o instanceof Coord && ((Coord) o).i == i && ((Coord) o).j == j;
		}

		public int hashCode() {
			int hashCode = 1;
			hashCode = 31 * hashCode + i;
			hashCode = 31 * hashCode + j;
			return hashCode;
		}
	}

	private Set<Coord> gameOfLife2DInfinite(Set<Coord> live) {
		Map<Coord, Integer> neighbours = new HashMap<>();
		for (Coord cell : live) {
			// for each living cell go around all 8 sides to the neighbors and
			// add 1 to their count
			for (int i = cell.i - 1; i < cell.i + 2; i++) {
				for (int j = cell.j - 1; j < cell.j + 2; j++) {
					if (i == cell.i && j == cell.j)
						continue;
					Coord c = new Coord(i, j);
					if (neighbours.containsKey(c)) {
						neighbours.put(c, neighbours.get(c) + 1);
					} else {
						neighbours.put(c, 1);
					}
				}
			}
		}
		Set<Coord> newLive = new HashSet<>();
		for (Map.Entry<Coord, Integer> cell : neighbours.entrySet()) {
			// if a cell has value 3 that means it had 3 cells alive in previous
			// round so it now becomes alive.
			// that covers the case whether it was dead->alive or alive->stay
			// alive.
			// otherwise if it has 2 neighbors alive it must have been alive to
			// start with (this is to exclude the case where the cell was dead
			// to begin with but now has 2 neighbors then we don't want to make
			// it alive again)
			if ((cell.getValue() == 3) || (cell.getValue() == 2 && live.contains(cell.getKey()))) {
				newLive.add(cell.getKey());
			}
		}
		return newLive;
	}

	private static void gameOfLife(String input) {
		int[] current = new int[input.length()];
		char[] inputArray = input.toCharArray();
		for (int i = 0; i < inputArray.length; i++) {
			current[i] = (inputArray[i] == '1' ? 1 : 0);
		}

		System.out.println("Starting GOL for " + input);

		tryState(0, 0, current);
		tryState(0, 1, current);
		tryState(1, 0, current);
		tryState(1, 1, current);

		System.out.println("Done with GOL for " + input);
	}

	private static void gameOfLifeRotation(String input) {
		System.out.println("Starting GOL rotation for " + input);

		int cur = Integer.parseInt(input, 2);

		int orig = 0;
		for (int i = 0; i < input.length(); i++) {
			if ((i % 3) != (2 * input.length() % 3)) {
				int rotans = leftRotate(cur, i, input.length());
				orig ^= rotans;
				System.out.println(
						"i " + i + " orig " + Integer.toBinaryString(orig) + " rot " + Integer.toBinaryString(rotans));
			}
		}

		if ((input.length() % 3) == 0) {
			if (orig == 0)
				System.out.println("Multiple solutions");
			else
				System.out.println("No solution");
		} else {
			String origString = Integer.toBinaryString(orig);
			// left pad any zeros
			for (int j = 0; j < (input.length() - origString.length()); j++)
				System.out.print('0');
			System.out.println(origString);
		}

		System.out.println("Done with GOL rotation for " + input);
	}

	private static int leftRotate(int current, int amt, int N) {
		/*
		 * In current << amt, last amt bits are 0. To put first amt bits of
		 * current at last, do bitwise or of current << amt with amt >>(LENGTH
		 * i.e N - amt)
		 */
		return (current << amt) | (current >> (N - amt));
	}

	private static void tryState(int first, int second, int[] current) {

		int[] original = new int[current.length];
		original[0] = first;
		original[1] = second;
		for (int k = 2; k < original.length - 1; k++) {
			original[k] = original[k - 2] ^ current[k - 1] ^ original[k - 1];
		}
		original[original.length - 1] = current[original.length - 1] ^ original[original.length - 2] ^ original[0];

		// rebuild
		int[] rebuild = new int[original.length];
		for (int k = 1; k < rebuild.length - 1; k++) {
			rebuild[k] = original[k] ^ original[k - 1] ^ original[k + 1];
		}
		rebuild[0] = original[0] ^ original[1] ^ original[original.length - 1];
		rebuild[rebuild.length - 1] = original[original.length - 1] ^ original[0] ^ original[original.length - 2];

		if (Arrays.equals(rebuild, current)) {
			System.out.println(Arrays.toString(original));
		}
	}

	public static void main(String[] args) throws java.lang.Exception {

		gameOfLife1D(new int[] { 0, 1, 1, 0, 0, 1, 0, 1 });
		gameOfLife1D(new int[] { 1, 0, 0, 1, 0 });

		gameOfLife("00011101");
		gameOfLife("000");
		gameOfLife("000001");
		gameOfLife("11110");

		gameOfLifeRotation("00011101");
		gameOfLifeRotation("000");
		gameOfLifeRotation("000001");
		gameOfLifeRotation("11110");
	}
}
