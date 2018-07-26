package dp;

public class PowerOfFour {

	private static boolean isPowerOfFour(int number) {

		boolean oneBitSet = ((number & (number - 1)) == 0);
		int count = 0;
		while (number > 1) {			
			number >>= 1;
			count++;
		}
		boolean numberOfBitsSetAfterMSBIsEven = count % 2 == 0;
		return oneBitSet && numberOfBitsSetAfterMSBIsEven;
	}
	
	private static boolean isPowerOfFourBitMask(int number) {

		boolean oneBitSet = ((number & (number - 1)) == 0);
		return oneBitSet && ((number & 0x55555555) == number);
	}

	public static void main(String[] args) {
		System.out.println("2 is power of 4 " + isPowerOfFourBitMask(2));
		System.out.println("4 is power of 4 " + isPowerOfFourBitMask(4));
		System.out.println("1 is power of 4 " + isPowerOfFourBitMask(1));
		System.out.println("0 is power of 4 " + isPowerOfFourBitMask(0));
		System.out.println("16 is power of 4 " + isPowerOfFourBitMask(16));
		System.out.println("8 is power of 4 " + isPowerOfFourBitMask(8));
		System.out.println("5 is power of 4 " + isPowerOfFourBitMask(5));
	}

}
