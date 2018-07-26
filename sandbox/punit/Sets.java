package dp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.BitSet;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Sets {
	
	public static void generate(String[][] sets) {
		int solutions = 1;
		for (int i = 0; i < sets.length; solutions *= sets[i].length, i++)
			;
		for (int i = 0; i < solutions; i++) {
			int j = 1;
			for (String[] set : sets) {
				System.out.print(set[(i / j) % set.length] + " ");
				j *= set.length;
			}
			System.out.println();
		}

		System.out.println("number of solutions is " + solutions);
	}
	
	private static void getSubsetsSizeK(List<Integer> superSet, int k, int idx, List<Integer> current,List<List<Integer>> solution) {
		//successful stop clause		
	    if (current.size() == k) {
	        solution.add(new ArrayList<>(current));
	        return;
	    }
	    
	    //unsuccessful stop clause
	    if (idx == superSet.size()) return;
	    Integer x = superSet.get(idx);
	    current.add(x);
	    //"guess" x is in the subset
	    getSubsetsSizeK(superSet, k, idx+1, current, solution);
	    current.remove(x);
	    //"guess" x is not in the subset
	    getSubsetsSizeK(superSet, k, idx+1, current, solution);
	}

	private static void getSubsetsSizeK(List<Integer> superSet, int k) {
	    List<List<Integer>> res = new ArrayList<>();
	    getSubsetsSizeK(superSet, k, 0, new ArrayList<Integer>(), res);
	    
	    System.out.println("Number of subsets of size " + k + " is " + res.size());
	    for (List<Integer> subset : res) {
	    	System.out.println(subset);
	    }
	}
	
	private static void getSubsets(List<Integer> superSet, int idx, Set<Integer> current,List<Set<Integer>> solution) {
		//successful stop clause		
	    if (idx == superSet.size()) {
	        solution.add(new HashSet<>(current));
	        return;
	    }
	    
	    Integer x = superSet.get(idx);
	    current.add(x);
	    //"guess" x is in the subset
	    getSubsets(superSet, idx+1, current, solution);
	    current.remove(x);
	    //"guess" x is not in the subset
	    getSubsets(superSet, idx+1, current, solution);
	}

	private static void getSubsets(List<Integer> superSet) {
	    List<Set<Integer>> res = new ArrayList<>();
	    getSubsets(superSet, 0, new HashSet<Integer>(), res);
	    
	    System.out.println("Number of subsets is " + res.size());
	    for (Set<Integer> subset : res) {
	    	System.out.println(subset);
	    }
	}
	
	private static void stringSubsets(String input, int k, int index, StringBuilder builder) {
		if (builder.length() == k) {
			System.out.println(builder.toString());
			return;
		}
		
		if (index == input.length()) {
			return;
		}
		
		builder.append(input.charAt(index));
		stringSubsets(input, k, index+1, builder);
		builder.deleteCharAt(builder.length()-1);
		stringSubsets(input, k, index+1, builder);
	}
	
	private static void stringPermute(StringBuilder input, int left, int right) {
		
		if (left == right) {
			System.out.println(input.toString());
			return;
		}
		
		for (int i = left; i <= right; i++) {
			char leftChar = input.charAt(left);
			char ithChar = input.charAt(i);
			input.setCharAt(left, ithChar);
			input.setCharAt(i, leftChar);
			stringPermute(input, left+1, right);
			input.setCharAt(left, leftChar);
			input.setCharAt(i, ithChar);			
		}
	}
	
	private static void getSubsetsV2(List<Integer> superSet) {		
		List<List<Integer>> all = getSubsetsV2(superSet,0);
		
		System.out.println("Number of v2 subsets is " + all.size());
	    for (List<Integer> subset : all) {
	    	System.out.println(subset);
	    }
	}
	
	private static List<List<Integer>> getSubsetsV2(List<Integer> superSet, int index) {
		List<List<Integer>> all = null;
		if (index == superSet.size()) {
			all = new ArrayList<List<Integer>>();
			all.add(new ArrayList<Integer>());
			return all;
		}
		int val = superSet.get(index);
		all = getSubsetsV2(superSet,index+1);
		List<List<Integer>> addl = new ArrayList<List<Integer>>();
		for (List<Integer> current : all) {
			List<Integer> another = new ArrayList<Integer>();
			another.add(val);
			another.addAll(current);
			addl.add(another);
		}
		all.addAll(addl);
		return all;
	}
	
	
	private static void getSubsetsV2SizeK(List<Integer> superSet, int size) {		
		int total = 1 << superSet.size(); // 2^ superset size
		List<List<Integer>> all = new ArrayList<List<Integer>>();
		for (int i = 0; i < total; i++) {
			List<Integer> sub = new ArrayList<Integer>();
			int idx=0;
			// for each bit that is set in the ith binary number
			// add that many elements from the original set into a new subset
			for (int j = i; j > 0; j >>= 1) {
				if ((j & 1) == 1) {
					sub.add(superSet.get(idx));
				}
				idx++;
			}
			if (sub.size() == size) {
				all.add(sub);
			}
		}
		
		System.out.println("Number of v2 subsets of size " + size + " is " + all.size());
	    for (List<Integer> subset : all) {
	    	System.out.println(subset);
	    }
	}
	
	private static void getSubsetsV3(List<Integer> input) {
		List<List<Integer>> all = new ArrayList<List<Integer>>();
		List<Integer> empty = new ArrayList<>();
		all.add(empty);
		
		for (Integer i : input) {
			List<List<Integer>> sub = new ArrayList<List<Integer>>();			
			for (List<Integer> existing : all) {
				List<Integer> addl = new ArrayList<Integer>(existing);
				addl.add(i);
				sub.add(addl);
			}
			all.addAll(sub);
		}
		
		System.out.println("Number of v3 subsets is " + all.size());
	    for (List<Integer> subset : all) {
	    	System.out.println(subset);
	    }
	}
	
	// generate power set where you don't have to store all elements upfront
	public static class PowerSet<E> implements Iterator<Set<E>>,Iterable<Set<E>>{
	    private E[] arr = null;
	    private BitSet bset = null;

	    @SuppressWarnings("unchecked")
	    public PowerSet(Set<E> set)
	    {
	        arr = (E[])set.toArray();
	        bset = new BitSet(arr.length + 1);
	    }

	    @Override
	    public boolean hasNext() {
	        return !bset.get(arr.length);
	    }

	    @Override
	    public Set<E> next() {
	        Set<E> returnSet = new TreeSet<E>();
	        for(int i = 0; i < arr.length; i++)
	        {
	            if(bset.get(i))
	                returnSet.add(arr[i]);
	        }
	        //increment bset
	        for(int i = 0; i < bset.size(); i++)
	        {
	            if(!bset.get(i))
	            {
	                bset.set(i);
	                break;
	            }else
	                bset.clear(i);
	        }

	        return returnSet;
	    }

	    @Override
	    public void remove() {
	        throw new UnsupportedOperationException("Not Supported!");
	    }

	    @Override
	    public Iterator<Set<E>> iterator() {
	        return this;
	    }

	};

	public static void main(String[] args) throws java.lang.Exception {
		String[] set1 = { "PUT", "CALL", "OPT" };
		String[] set2 = { "1", "2", "3", "4" };
		String[] set3 = { "BUY", "SELL" };
		String[][] allsets = { set1, set2, set3 };
		generate(allsets);
		
		getSubsetsSizeK(Arrays.asList(1,2,3), 2);
		getSubsetsV2SizeK(Arrays.asList(1,2,3), 2);
		
		getSubsets(Arrays.asList(1,2,3));
		getSubsetsV2(Arrays.asList(1,2,3));
		getSubsetsV3(Arrays.asList(1,2,3));
		
		System.out.println("Printing all subsets");
		Set<Integer> orig = new HashSet<Integer>();
		orig.addAll(Arrays.asList(1,2,3));
		PowerSet<Integer> ps = new PowerSet<Integer>(orig);
		while (ps.hasNext()) {
			System.out.println(ps.next());
		}
		
		//stringSubsets("abc", 1, 0, new StringBuilder());
				
		stringPermute(new StringBuilder("abc"), 0, 2);
	}
	

}
