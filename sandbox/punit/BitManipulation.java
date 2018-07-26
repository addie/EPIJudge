package dp;

public class BitManipulation {

	private static void addOne(int num) {
		System.out.println(Integer.toBinaryString(num));
		System.out.println(Integer.toBinaryString(-num));
		System.out.println(Integer.toBinaryString(~num));
		System.out.println(Integer.toBinaryString(-~num));
		int res = -(~(num));
		System.out.println(res);
	}
	
	private static void add1(int num) {
		
		// flip rightmost zero to 1
		// any ones along the way turn to zero
		int m = 1;
		while ((num &m) == m) {
			num = num ^ m;
			m <<= 1;
		}
		
		num ^= m;
		System.out.println(num);		
	}
	
	public static void main(String[] args) {
		add1(5);
		add1(1);
		add1(0);
		add1(2);
		addOne(Integer.MAX_VALUE);
	}

}
