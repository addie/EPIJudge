package dp;

public class PredictWinner {

	public boolean PredictTheWinner(int[] nums) {
		Integer[][] memo = new Integer[nums.length][nums.length];
		return winner(nums, 0, nums.length - 1, memo) >= 0;
	}

	private int winner(int[] nums, int s, int e, Integer[][] memo) {
		if (s == e)
			return nums[s];
		if (memo[s][e] != null)
			return memo[s][e];
		// take from the front or back and take the better of the two outcomes
		// subtract the remaining as you assume the other person will gain the
		// rest of it in the next turn
		int a = nums[s] - winner(nums, s + 1, e, memo);
		int b = nums[e] - winner(nums, s, e - 1, memo);
		memo[s][e] = Math.max(a, b);
		return memo[s][e];
	}

}
