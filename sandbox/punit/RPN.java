package dp;

import java.util.Stack;

public class RPN {

	public enum Operator {
		ADD("+") {
			@Override
			public Integer apply(Integer left, Integer right) {
				return left + right;
			}
		},
		SUBTRACT("-") {
			@Override
			public Integer apply(Integer left, Integer right) {
				return left - right;
			}
		},
		MULTIPLY("*") {
			@Override
			public Integer apply(Integer left, Integer right) {
				return left * right;
			}
		},
		DIVIDE("/") {
			@Override
			public Integer apply(Integer left, Integer right) {
				return left / right;
			}
		};

		private String symbol;

		private Operator(String symbol) {
			this.symbol = symbol;
		}

		public static Operator getOperator(String symbol) {
			for (Operator o : values()) {
				if (o.symbol.equals(symbol)) {
					return o;
				}
			}

			return null;
		}

		public abstract Integer apply(Integer left, Integer right);
	}

	public int solve(String expression) {
		String[] tokens = expression.split(" ");
		Stack<Integer> operand = new Stack<>();
		for (String token : tokens) {
			Operator op = Operator.getOperator(token);
			if (op != null) {
				Integer first = operand.pop();
				Integer second = operand.pop();
				Integer result = Operator.getOperator(token).apply(first, second);
				operand.push(result);
			} else {
				operand.push(Integer.parseInt(token));
			}
		}

		return operand.pop();
	}

	public static void main(String[] args) {
		RPN calc = new RPN();
		System.out.println(calc.solve("4 3 +"));
		System.out.println(calc.solve("4 3 -"));
		System.out.println(calc.solve("4 3 + 7 *"));
	}

}
