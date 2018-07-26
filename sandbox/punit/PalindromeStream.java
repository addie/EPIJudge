package dp;

import java.math.BigDecimal;

public class PalindromeStream {

	private StringBuilder stream;

	private int leftHash;
	private int rightHash;
	private int h = 1;

	private final int PRIME = 103;
	private final int BASE = 256;

	public PalindromeStream() {
		stream = new StringBuilder();
		leftHash = 0;
		rightHash = 0;
	}

//@formatter:off
	
	/*
	 * abcba
	 * 
	 * a = 32, b = 33, c = 34, d = 35, e = 36
	 * 
	 * 3^0 * a   -------  3^0 * a
	 * 3^0 * a + 3^1 * b  ------  3^0 * b + 3^1 * a
	 * 3^0 * a + 3^1 * b + 3^2 * c  ------  3^0 * c + 3^1 * b + 3^2 * a
	 * 3^0 * a + 3^1 * b + 3^2 * c + 3^3 * b  ------  3^0 * b + 3^1 * c + 3^2 * b + 3^3 * a
	 * 3^0 * a + 3^1 * b + 3^2 * c + 3^3 * b + 3^4 * a  ------  3^0 * a + 3^1 * b + 3^2 * c + 3^3 * b + 3^4 a 
	 * 
	 * 
	 */
	
//@formatter:on	

	
	private BigDecimal bdl = new BigDecimal(0);
	private BigDecimal bdr = new BigDecimal(0);
	public boolean isPalindrome(char c) {
		stream.append(c);
	
		bdl = bdl.add(new BigDecimal(BASE).pow(stream.length()-1).multiply(new BigDecimal(c)));				
		bdr = bdr.multiply(new BigDecimal(BASE)).add(new BigDecimal(c));

		// causes overflow
		//leftHash += Math.pow(BASE, stream.length() - 1) * c;
		//rightHash = rightHash * BASE + c;
		
		leftHash = bdl.intValue();
		rightHash = bdr.intValue();
		System.out.println("left " + leftHash + " right " + rightHash);

		if (leftHash == rightHash) {
			// check entire string
			int i = 0;
			int j = stream.length() - 1;

			while (i < j) {
				if (stream.charAt(i) != stream.charAt(j)) {
					return false;
				}
				i++;
				j--;
			}
			return true;
		} else {
			return false;
		}
	}

	public boolean isPalindromeV2(char c) {
		stream.append(c);

		if (stream.length() == 1) {
			leftHash = stream.charAt(0) % PRIME;
			return true;
		} else if (stream.length() == 2) {
			rightHash = stream.charAt(1) % PRIME;
		} else {

			boolean evenLength = stream.length() % 2 == 0;
			if (evenLength) {

				// incrementally increase the power rather than recompute each time
				h = (h * BASE) % PRIME;
				// add in character to the left of the middle to left
				leftHash = (leftHash + stream.charAt((stream.length()-1) / 2) * h) % PRIME;
				// add in last character to the right
				rightHash = (rightHash * BASE + c) % PRIME;

			} else {
				// remove middle character from right and add in last character				
				rightHash = (BASE * (rightHash - h * stream.charAt(stream.length() / 2)) % PRIME + c) % PRIME;
			}
		}

		//System.out.println("left " + leftHash + " right " + rightHash);

		return leftHash == rightHash;
	}

	public static void main(String[] args) {
		String testString = "mmmmmmmmmmmmmKKKKKKRRRyyyzzzaabaacaabaazzzyyyRRRKKKKKKmmmmmmmmmmmmm";
		//String testString = "abeba";
		PalindromeStream stream = new PalindromeStream();
		for (int index = 0; index < testString.length(); index++) {
			boolean val = stream.isPalindromeV2(testString.charAt(index));
			System.out.println(testString.substring(0, index + 1) + " ---> " + val);
		}
	}

}
