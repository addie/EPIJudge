package dp;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Xor {

	private class XorPair implements Comparable<XorPair> {
		int first;
		int second;
		int bitSum;

		public int compareTo(XorPair other) {
			return other.bitSum - bitSum;
		}

		public String toString() {
			return "(" + first + ", " + second + ") ->" + bitSum;
		}
	}

	private int countBits(int num) {
		int counter = 0;
		while (num > 0) {
			if ((num & 1) == 1) {
				counter++;
			}
			num = num >> 1;
		}
		return counter;
	}

	private int max(int n, int m) {

		List<XorPair> list = new ArrayList<XorPair>();
		Set<Integer> nums = new HashSet<Integer>();
		// generate all possible pairs
		for (int i = 1; i < n; i++) {
			for (int j = i + 1; j <= n; j++) {
				XorPair pair = new XorPair();
				pair.first = i;
				pair.second = j;
				int xor = i ^ j;
				int sumBits = countBits(xor);
				pair.bitSum = sumBits;
				list.add(pair);
			}
		}
		Collections.sort(list);
		for (XorPair x : list) {
			nums.add(x.first);
			if (nums.size() == m) {
				break;
			}
			nums.add(x.second);
			if (nums.size() == m) {
				break;
			}
		}
		
		System.out.println("Numbers included " + nums);
		
		// go through all pairs that have nums and form max sum
		int maxSum = 0;
		for (XorPair x : list) {
			if (nums.contains(x.first)  && nums.contains(x.second)) {
				maxSum += x.bitSum;
			}
		}

		return maxSum;
	}

	private void getSubsetsSizeK(List<Integer> superSet, int size) {
		int total = 1 << superSet.size(); // 2^ superset size
		List<List<Integer>> all = new ArrayList<List<Integer>>();
		for (int i = 0; i < total; i++) {
			List<Integer> sub = new ArrayList<Integer>();
			int idx = 0;
			// for each bit that is set in the ith binary number
			// add that many elements from the original set into a new subset
			for (int j = i; j > 0; j >>= 1) {
				if ((j & 1) == 1) {
					sub.add(superSet.get(idx));
				}
				idx++;
			}
			if (sub.size() == size) {
				all.add(sub);
			}
		}

		System.out.println("Number of subsets of size " + size + " is " + all.size());
		int maxSum = 0;
		List<Integer> maxSubset = null;
		for (List<Integer> subset : all) {

			int sum = 0;
			for (int i = 0; i < subset.size() - 1; i++) {
				for (int j = i + 1; j < subset.size(); j++) {
					int xor = subset.get(i) ^ subset.get(j);
					int sumBits = countBits(xor);
					sum += sumBits;
				}
			}
			if (maxSum < sum) {
				maxSum = sum;
				maxSubset = subset;
			}
		}
		System.out.println("max sum is " + maxSum + " formed by subset " + maxSubset);
	}

	public static void main(String[] args) {

		Xor x = new Xor();
		System.out.println("n = 10, m = 8, max = " + x.max(10, 8));
		// System.out.println("n = 10, m = 6, max = " + x.max(10, 6));

		List<Integer> superSet = new ArrayList<>();
		for (int i = 1; i <= 10; i++) {
			superSet.add(i);
		}
		x.getSubsetsSizeK(superSet, 8);
	}

}
