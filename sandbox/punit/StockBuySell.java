package dp;

public class StockBuySell {

	private int maxProfit(int[] prices, int k) {

		//@formatter:off
		
		// dp[i,j] means for i transactions up till the jth day, the max profit
		int dp[][] = new int[k+1][prices.length];
		
		// base case:
		// dp[0,j] ==> 0 transactions means 0 profit on all days
		// dp[i, 0] ==> 0 days means 0 profit on all transactions (can't make any profit with only single price)
		
		// recurrence
		// dp[i][j] = max { dp[i][j-1], // don't do anything on the jth day
		//				  {	prices[j] - prices[m] + dp[i-1][m] // buy on the mth day and sell on the jth day
															   // plus the profit from 1 less transaction up to the mth day
															   // m = 0.. j-1

		//@formatter:on

		for (int i = 1; i <= k; i++) {
			for (int j = 1; j < prices.length; j++) {
				int mthdaybuy = 0;
				for (int m = 0; m < j; m++) {
					mthdaybuy = Math.max(mthdaybuy, prices[j] - prices[m] + dp[i - 1][m]);
				}
				dp[i][j] = Math.max(dp[i][j - 1], mthdaybuy);
			}
		}

		return dp[k][prices.length - 1];
	}

	/**
	 * If I am holding a share after today, then either I am just continuing
	 * holding the share I had yesterday, or that I held no share yesterday, but
	 * bought in one share today: hold = max(hold, cash - prices[i]). 
	 * If I am not holding a share after today, then either I did not hold a share
	 * yesterday, or that I held a share yesterday but I decided to sell it out
	 * today: cash = max(cash, hold + prices[i] - fee).
	 */
	public int maxProfitWithFee(int[] prices, int fee) {
		int cash = 0, hold = -prices[0];
		for (int i = 1; i < prices.length; i++) {
			cash = Math.max(cash, hold + prices[i] - fee);
			hold = Math.max(hold, cash - prices[i]);
		}
		return cash;
	}

	private int maxProfitOneTransaction(int[] prices) {
		int profit = 0;
		int minPrice = prices[0];
		for (int i = 1; i < prices.length; i++) {
			profit = Math.max(profit, prices[i] - minPrice);
			minPrice = Math.min(minPrice, prices[i]);
		}
		return profit;
	}

	private int maxProfitTwoTransactions(int[] prices) {
		int buySells[] = new int[prices.length];
		int minPrice = prices[0];
		int profit = 0;
		// best running profit with one transaction
		for (int i = 1; i < prices.length; i++) {
			minPrice = Math.min(minPrice, prices[i]);
			profit = Math.max(profit, prices[i] - minPrice);
			buySells[i] = profit;
		}

		//@formatter:off
	
		// find profit for second buy
		// if you buy on the jth day, then you pay out prices[j] and you can gain the highest price for any day k, k > j
		// that's why it goes backwards
		// add to that the max profit you have from the previous (1) transaction which would be at day j-1
		
		// also, don't reset the max profit because we might not even do a second transaction at all
		// i.e. if there is only one price increase then all decrease, we would never find a second transaction
		// if we reset the profit then we'd end up with zero
		
		//@formatter:on

		int maxPrice = prices[prices.length - 1];
		// start at -2 because you can't end with a buy
		for (int j = prices.length - 2; j > 0; j--) {
			maxPrice = Math.max(maxPrice, prices[j]);
			profit = Math.max(profit, maxPrice - prices[j] + buySells[j - 1]);
		}
		return profit;
	}

	public static void main(String[] args) {
		StockBuySell sbs = new StockBuySell();
		int k = 2;
		int prices[] = new int[] { 2, 5, 7, 1, 4, 3, 1, 8 };
		System.out.println("Max profit with " + k + " transactions is " + sbs.maxProfit(prices, k));
		System.out.println("Max profit with one transaction is " + sbs.maxProfitOneTransaction(prices));
		System.out.println("Max profit with two transactions is " + sbs.maxProfitTwoTransactions(prices));
	}

}
