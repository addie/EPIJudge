package dp;

public class SquareRoot {

	private static double root(double input) {

		if (input <= 0) {
			return Double.NaN;
		}
		
		double num = (double) input;
		double tolerance = 0.00001;
		double guess = 1;
		final int MAX_ITERATIONS= (int)Math.ceil(Math.log(input));
		int iterations=0;
		
	//	System.out.println("max iterations " + MAX_ITERATIONS);

		while (Math.abs(num - guess) > tolerance && iterations < MAX_ITERATIONS) {
			//num = guess + (num - guess) / 2;
			num = (num+guess)/2;
			guess = input / num;
			iterations++;
			//System.out.println("num " + num + " guess " + guess);
		}
		
	//	System.out.println("total iterations " + iterations);

		return num;
	}
	
	private static double newtonRoot(double input) {

		double c = input;
        double epsilon = 1e-15;    // relative error tolerance
        double t = c;              // estimate of the square root of c

        // repeatedly apply Newton update step until desired precision is achieved
        while (Math.abs(t - c/t) > epsilon*t) {
            t = (c/t + t) / 2.0;
      //      System.out.println("root estimate " + t);
      //      System.out.println("convergence check " + c/t);
      //      System.out.println("convergence check diff " + (t -c/t));
        }
        
        return t;
		
	}

	public static void main(String[] args) {
		System.out.println(root(Double.MAX_VALUE));
		System.out.println(newtonRoot(Double.MAX_VALUE));
		System.out.println(Math.sqrt(Double.MAX_VALUE));
		
		System.out.println(Double.MAX_VALUE);
		System.out.println(Double.MAX_VALUE+1d);
		
		System.out.println(root(Integer.MAX_VALUE));
		System.out.println(newtonRoot(Integer.MAX_VALUE));
		System.out.println(Math.sqrt(Integer.MAX_VALUE));
		
		System.out.println("-----------------");
		System.out.println(newtonRoot(64));
	}

}
