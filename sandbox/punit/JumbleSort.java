package dp;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class JumbleSort {

	private void jumbleSort(String line) {
		String[] tokens = line.split(" ");
		// separate tokens into lists of words and numbers
		List<String> strings = new ArrayList<String>();
		List<Integer> numbers = new ArrayList<Integer>();
		for (String token : tokens) {
			if (Character.isLetter(token.charAt(0))) {
				strings.add(token);
			} else {
				numbers.add(Integer.parseInt(token));
			}
		}
		
		Collections.sort(strings);
		Collections.sort(numbers);
		
		int stringCounter = 0;
		int numberCounter = 0;
		StringBuilder finalOutput = new StringBuilder();
		for (int i = 0; i < tokens.length; i++) {
			final String token = tokens[i];
			if (Character.isLetter(token.charAt(0))) {
				finalOutput.append(strings.get(stringCounter));
				stringCounter++;
			} else {
				finalOutput.append(numbers.get(numberCounter));
				numberCounter++;
			}
			if (i < tokens.length - 1) {
				finalOutput.append(" ");
			}
		}
		System.out.println(finalOutput.toString());
	}
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String line = scan.nextLine();
		scan.close();
		if (line == null || line.isEmpty()) {
			System.out.println();
		} else {
			new JumbleSort().jumbleSort(line);
		}

		
	}

}
