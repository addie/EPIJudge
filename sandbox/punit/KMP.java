package dp;

public class KMP {

	private int[] buildPrefixArray(char[] pattern) {
		int[] lps = new int[pattern.length];
		lps[0] = 0;

		int i = 1;
		int index = 0;
		for (; i < pattern.length;) {
			if (pattern[i] == pattern[index]) {
				lps[i] = index + 1;
				index++;
				i++;
			} else {
				if (index != 0) {
					index = lps[index - 1];
				} else {
					lps[i] = 0;
					i++;
				}
			}
		}
		return lps;
	}

	private void runKMP(char[] text, char[] pattern) {
		int[] lps = buildPrefixArray(pattern);

		int i = 0;
		int j = 0;
		while (i < text.length) {

			if (text[i] == pattern[j]) {
				i++;
				j++;
			}

			if (j == pattern.length) {
				System.out.println("Match found at " + (i - pattern.length));
				j = lps[j - 1];
			} else if (i < text.length && text[i] != pattern[j]) {
				if (j != 0) {
					j = lps[j - 1];
				} else {
					i++;
				}
			}
		}
	}

	public static void main(String[] args) {
		KMP kmp = new KMP();
		kmp.runKMP("abcabcabc".toCharArray(), "abc".toCharArray());

	}

}
