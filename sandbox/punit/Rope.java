package dp;

public class Rope {
	
	public class RopeNode {
		public String text;
		public int weight;
		public RopeNode left;
		public RopeNode right;
		
		public String toString() {
			return text + " (" + weight + ")" + "[" + left + "], " + "[" + right + "]";
		}
	}
	
	public RopeNode buildTree(String input) {
		
		if (input == null) {
			return null;
		}
		
		RopeNode root = new RopeNode();		
		if (input.length() <= 5) {
			root.text = input;
			root.weight = input.length();			
		} else {
			root.left = buildTree(input.substring(0, input.length()/2));
			root.right = buildTree(input.substring(input.length()/2));
			root.weight = input.length()/2;
		}
		
		return root;
	}
	
	// get the character at the index given
	public char index(RopeNode root, int index) {
		if (index >= root.weight) {
			return index(root.right, index - root.weight);
		} else {
			if (root.left == null) {
				return root.text.charAt(index);
			} else {
				return index(root.left, index);
			}
		}
	}
	
	public static void main(String[] args) {
		Rope rope = new Rope();
		String input = "hello world how are you today? good - how about some booogers for you? yeah!";
		RopeNode root = rope.buildTree(input);
		System.out.println(root);
		for (int i = 0; i < input.length(); i++) {
			System.out.print(rope.index(root, i));
		}
		System.out.println();
	}
	

}
