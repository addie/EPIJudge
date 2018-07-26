package dp;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

public class WordChain {
	
	public int getLength(String[] words) {
		if (words.length == 0) {
			return 0;
		}
		
		Arrays.sort(words, new Comparator<String>() {
			@Override
			public int compare(String o1, String o2) {
				return o1.length() - o2.length();
			}
		});
		
		Map<String,Integer> map = new HashMap<>();
		map.put(words[0], 0);
		
		int[] dp = new int[words.length+1];
		dp[0] = 1;		
		int maxLength = dp[0];
		
		for (int i = 1; i < words.length; i++) {
			dp[i] = 1;
			String word = words[i];
			for (int j = 0; j < word.length(); j++) {
				StringBuilder tempb = new StringBuilder(word);
				tempb.deleteCharAt(j);
				String temp = tempb.toString();
				if (map.containsKey(temp)) {
					dp[i] = Math.max(dp[i], dp[map.get(temp)]+1);
				}
			}
			maxLength = Math.max(maxLength, dp[i]);
			map.put(word, i);
		}
		
		return maxLength;
	}

	public static void main(String[] args) {
		String[] words = new String[] {"a","b","ba","bca","bda","bdca"};
		WordChain chain = new WordChain();
		System.out.println(chain.getLength(words));
	}
	
}
