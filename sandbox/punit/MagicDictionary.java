package dp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class MagicDictionary {

	private static class Node {
		public Map<Character, Node> children;
		public boolean isTerminal;
		public char value;

		public Node() {
			children = new HashMap<Character, Node>();
			isTerminal = false;
		}
		
		public String toString() {
			return String.valueOf(value) + " --> " + children.values();
		}
	};

	private Node dummyRoot;

	/** Initialize your data structure here. */
	public MagicDictionary() {
		dummyRoot = new Node();
	}

	/** Build a dictionary through a list of words */
	public void buildDict(String[] dict) {
		for (String word : dict) {
			char[] letters = word.toCharArray();
			Node starting = dummyRoot;
			for (int i = 0; i < letters.length; i++) {
				starting = addNode(starting.children, i, letters);
			}
		}
	}

	private Node addNode(Map<Character, Node> map, int index, char[] letters) {
		char starting = letters[index];
		Node root = map.get(starting);
		if (root == null) {
			root = new Node();
			root.value = starting;
			map.put(starting, root);
		}
		if (index == letters.length - 1) {
			root.isTerminal = true;
		}
		return root;
	}

	/**
	 * Returns if there is any word in the trie that equals to the given word
	 * after modifying exactly one character
	 */
	public boolean search(String word) {
		if (word.length() < 1) {
			return false;
		}

		System.out.println("searching for " + word);

		char[] letters = word.toCharArray();
		boolean skippedOne = false;
		List<Node> searchNodes = new ArrayList<>();
		searchNodes.add(dummyRoot);

		for (int i = 0; i < letters.length; i++) {
			char searchLetter = letters[i];
			List<Node> nextPath = new ArrayList<Node>();
			for (Node search : searchNodes) {
				System.out.println("Searching from node " + search.value);
				Node potential = search.children.get(searchLetter);
				if (potential != null && potential.isTerminal && i == letters.length - 1) {
					return true;
				} else if (potential != null) {
					nextPath.add(potential);
				} else {

				}
			}

			if (nextPath.isEmpty() && !skippedOne) {
				for (Node search : searchNodes) {
					nextPath.addAll(search.children.values());
				}
				skippedOne = true;
			} else if (nextPath.isEmpty() && skippedOne) {
				System.out.println("Already skipped and no more potential matches");
				return false;
			}

			searchNodes.clear();
			searchNodes.addAll(nextPath);
			nextPath.clear();
		}

		System.out.println("not found");
		return false;
	}

	public static void main(String[] args) {
		MagicDictionary obj = new MagicDictionary();
		String[] dict = {"hello","leetcode"};
		obj.buildDict(dict);
		String word = "hello";
		boolean param_2 = obj.search(word);
		System.out.println(param_2);
	}

}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary(); obj.buildDict(dict); boolean
 * param_2 = obj.search(word);
 */