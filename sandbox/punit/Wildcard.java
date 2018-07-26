package dp;

public class Wildcard {

	public boolean matches(String pattern, String text) {

		int p = 0;
		int match = 0;
		int s = 0;
		int starIdx = -1;
		while (s < text.length()) {

			if (p < pattern.length() && (pattern.charAt(p) == '?' || pattern.charAt(p) == text.charAt(s))) {
				p++;
				s++;
			} else if (p < pattern.length() && pattern.charAt(p) == '*') {
				starIdx = p;
				match = s;
				p++;
			} else if (starIdx != -1) {
				p = starIdx + 1;
				match++;
				s = match;
			} else {
				return false;
			}
		}

		while (p < pattern.length() && pattern.charAt(p) == '*') {
			p++;
		}

		return p == pattern.length();
	}

	public boolean matchesDP(String p, String s) {

		boolean[][] match = new boolean[s.length() + 1][p.length() + 1];
		match[0][0] = true;

		for (int i = 1; i <= p.length(); i++)
			if (p.charAt(i - 1) == '*')
				match[0][i] = match[0][i - 1];

		for (int i = 1; i <= s.length(); i++)
			for (int j = 1; j <= p.length(); j++) {
				if (p.charAt(j - 1) == '?' || (s.charAt(i - 1) == p.charAt(j - 1))) {
					match[i][j] = match[i - 1][j - 1];
				} else if (p.charAt(j - 1) == '*') {
					match[i][j] = match[i][j - 1] || match[i - 1][j];
				}
			}
		return match[s.length()][p.length()];
	}

	public static void main(String[] args) {
		Wildcard wild = new Wildcard();
		System.out.println(wild.matchesDP("**b***aaaa******", "sadfzvsddfbsdfaaaa23523"));
		System.out.println(wild.matchesDP("*", ""));
		System.out.println(wild.matchesDP("a?a", "aaa"));

	}

}
