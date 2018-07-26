package dp;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class CopyFile {

	private List<Integer> tokenizeDataSetIds(String datasetIds) {
		String[] ids = datasetIds.split(" ");
		List<Integer> dsids = new ArrayList<Integer>(ids.length);
		for (int i = 1; i < ids.length; i++) {
			dsids.add(Integer.parseInt(ids[i]));
		}
		Collections.sort(dsids);
		return dsids;
	}
	
	private void runCopy(Map<Integer,List<Integer>> dataCenterToDataSets, Set<Integer> alldsids) {
		
		List<Integer> alldsidsSorted = new ArrayList<Integer>(alldsids);
		Collections.sort(alldsidsSorted);
		
		// build a Map that indicates for each data set id, which (any) data center contains it
		Map<Integer,Integer> dataSetIdToDataCenter = new HashMap<Integer,Integer>();
		for (Integer dataCenter : dataCenterToDataSets.keySet()) {			
			List<Integer> dataSets = dataCenterToDataSets.get(dataCenter);
			for (Integer ds : dataSets) {
				if (!dataSetIdToDataCenter.containsKey(ds)) {
					dataSetIdToDataCenter.put(ds, dataCenter);
				}
			}
		}
		
		for (Integer dataCenter : dataCenterToDataSets.keySet()) {			
			List<Integer> dataSets = dataCenterToDataSets.get(dataCenter);	
			System.out.println("processing dataCenter " + dataCenter);
			System.out.println("currently contains " + dataSets);
			for (Integer dsId : alldsidsSorted) {								
				if (!dataSets.contains(dsId)) {				
					// missing this data set - copy it from someone
					Integer copyFrom = dataSetIdToDataCenter.get(dsId);
					System.out.println(dsId + " " + copyFrom + " " + dataCenter);
				}
			}
		}
		
		System.out.println("done");
	}
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		CopyFile cf = new CopyFile();
		int numberOfDataCenters = Integer.parseInt(scan.nextLine());
		Map<Integer,List<Integer>> dataCenterToDataSets = new HashMap<>();
		Set<Integer> alldsids = new HashSet<Integer>();
		for (int i = 0; i < numberOfDataCenters; i++) {
			String datasetIds = scan.nextLine();
			List<Integer> dsids = cf.tokenizeDataSetIds(datasetIds);
			dataCenterToDataSets.put(i+1, dsids);
			alldsids.addAll(dsids);
		}
		scan.close();
		cf.runCopy(dataCenterToDataSets, alldsids);
	}

}
