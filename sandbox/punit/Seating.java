package dp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Seating {

	public boolean canSeat(Set<Integer> seats, List<List<Integer>> prefs, int index) {
		
		if (index >= prefs.size()) {
			return true;
		}
		
		if (seats.isEmpty()) { 
			return false;
		}
		
		for (int j = index; j < prefs.size(); j++) {
			boolean found = false;
			for (Integer seat : prefs.get(j)) {
				if (seats.contains(seat)) {
					seats.remove(seat);
					found = canSeat(seats, prefs, j+1);					
					if (found) {
						return true;
					} else {
						seats.add(seat);
					}
				}
			}
			
			if (!found) {
				return false;
			}			
		}
		
		return true;
	}
	
	public static void main(String[] args) {
		Seating seat = new Seating();
		Set<Integer> allSeats = new HashSet<>();
		for (int i = 0; i < 4; i++) {
			allSeats.add(i);
		}
		
		List<List<Integer>> prefs = new ArrayList<>();
		prefs.add(Arrays.asList(0,1,2,3));
		prefs.add(Arrays.asList(3,2,1,0));
		prefs.add(Arrays.asList(0,1,2,3));
		prefs.add(Arrays.asList(3,2,1,0));
		
		System.out.println(seat.canSeat(allSeats, prefs, 0));
	}
}
