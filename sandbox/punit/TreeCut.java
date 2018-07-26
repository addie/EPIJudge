package dp;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class TreeCut {

	public static class TreeNode<T> {
		T value;
		int parentIndex;
		boolean inTree;

		public TreeNode(T value, int parentIndex) {
			this.value = value;
			this.parentIndex = parentIndex;
			this.inTree = true;
		}

		public String toString() {
			return value.toString() + " -> " + parentIndex + " - " + inTree;
		}
	};

	public <T> void remove(int index, List<TreeNode<T>> tree) {

		Set<T> visited = new HashSet<>();

		tree.get(index).inTree = false;
		visited.add(tree.get(index).value);

		for (TreeNode<T> node : tree) {
			if (visited.contains(node.value)) {
				continue;
			}

			boolean cut = cutTree(index, tree, node, visited);
			if (cut) {
				node.inTree = false;
			}
		}

		List<T> removed = new ArrayList<T>();
		for (TreeNode<T> node : tree) {
			if (!node.inTree) {
				removed.add(node.value);
			}
		}
		System.out.println(removed.size() + " -> " + removed);
	}

	private <T> boolean cutTree(int index, List<TreeNode<T>> tree, TreeNode<T> node, Set<T> visited) {
		if (!node.inTree || node.parentIndex == index) {
			return true;
		}

		if (node.parentIndex == -1 || visited.contains(node.value)) {
			return false;
		}

		boolean cut = cutTree(index, tree, tree.get(node.parentIndex), visited);
		visited.add(node.value);
		if (cut) {
			node.inTree = false;
		}
		return cut;
	}

	public <T> void removeV2(int index, List<TreeNode<T>> tree) {

		Set<T> visited = new HashSet<>();

		tree.get(index).inTree = false;
		visited.add(tree.get(index).value);

		for (TreeNode<T> node : tree) {
			if (visited.contains(node.value)) {
				continue;
			}

			cutTreeV2(tree, node, visited);
		}

		List<T> removed = new ArrayList<T>();
		for (TreeNode<T> node : tree) {
			if (!node.inTree) {
				removed.add(node.value);
			}
		}
		System.out.println(removed.size() + " -> " + removed);
	}

	private <T> boolean cutTreeV2(List<TreeNode<T>> tree, TreeNode<T> node, Set<T> visited) {
		if (node.parentIndex == -1 || visited.contains(node.value)) {
			visited.add(node.value); /// not necessary??
			return node.inTree;
		}

		visited.add(node.value);
		boolean cut = cutTreeV2(tree, tree.get(node.parentIndex), visited);
		if (node.inTree != cut) {
			node.inTree = cut;
		}
		return cut;
	}

	public static void main(String[] args) {

		TreeCut cut = new TreeCut();
		List<TreeNode<String>> tree = new ArrayList<>();
		tree.add(new TreeNode<String>("ROOT", -1)); // 0
		tree.add(new TreeNode<String>("A", 0)); // 1
		tree.add(new TreeNode<String>("D", 1)); // 2
		tree.add(new TreeNode<String>("C", 1)); // 3
		tree.add(new TreeNode<String>("K", 2)); // 4
		tree.add(new TreeNode<String>("V", 4));// 5
		tree.add(new TreeNode<String>("M", 7)); // 6
		tree.add(new TreeNode<String>("J", 2)); // 7
		tree.add(new TreeNode<String>("I", 3)); // 8
		tree.add(new TreeNode<String>("B", 1)); // 9
		tree.add(new TreeNode<String>("E", 9)); // 10
		tree.add(new TreeNode<String>("H", 12)); // 11
		tree.add(new TreeNode<String>("F", 9)); // 12
		tree.add(new TreeNode<String>("G", 12)); // 13
		tree.add(new TreeNode<String>("R", 20)); // 14
		tree.add(new TreeNode<String>("Y", 16)); // 15
		tree.add(new TreeNode<String>("O", 6)); // 16
		tree.add(new TreeNode<String>("N", 6)); // 17
		tree.add(new TreeNode<String>("L", 7)); // 18
		tree.add(new TreeNode<String>("S", 11)); // 19
		tree.add(new TreeNode<String>("P", 18)); // 20
		tree.add(new TreeNode<String>("Q", 20)); // 21
		tree.add(new TreeNode<String>("T", 13)); // 22
		tree.add(new TreeNode<String>("U", 13)); // 23
		tree.add(new TreeNode<String>("X", 6)); // 24
		tree.add(new TreeNode<String>("Z", 17)); // 25
		tree.add(new TreeNode<String>("W", 7)); // 26
		cut.remove(14, tree);
		cut.removeV2(14, tree);

		System.out.println("------");
		List<TreeNode<String>> tree2 = new ArrayList<>();
		tree2.add(new TreeNode<String>("E", 1)); // 0
		tree2.add(new TreeNode<String>("D", 2)); // 1
		tree2.add(new TreeNode<String>("C", 3)); // 2
		tree2.add(new TreeNode<String>("B", 4)); // 3
		tree2.add(new TreeNode<String>("A", -1)); // 4
		cut.remove(0, tree2);
		cut.removeV2(0, tree2);

	}
};
