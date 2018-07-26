package dp;

public class Matrix {
	
	private static void rotate(int[][] matrix) {
		
		int m = matrix.length-1;
		
		printMatrix(matrix);
		
		System.out.println("rotation");
		
		int[] swap = new int[4];		
		for (int layer = 0; layer <= m/2; layer++) {
			for (int x = layer; x < m - layer; x++) {
				
				swap[0] = matrix[layer][x]; // top left, going across
				swap[1] = matrix[x][m - layer]; // top right, going down
				swap[2] = matrix[m-layer][m-x]; // bottom right, going left
				swap[3] = matrix[m-x][layer]; // bottom left, going up
				
				matrix[layer][x] = swap[3];
				matrix[x][m-layer] = swap[0];
				matrix[m-layer][m-x] = swap[1];
				matrix[m-x][layer] = swap[2];
				
				//printMatrix(matrix);
			}
		}
		
		printMatrix(matrix);
	}
	
	private static void printMatrix(int[][] matrix) {
		for (int i = 0; i < matrix.length; i++) {
			for (int j =0 ; j < matrix[i].length; j++) {
				System.out.print(matrix[i][j]);
				System.out.print(",");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		int[][] matrix = new int[][] {{1,2,3,4},
									{5,6,7,8},
									{9,10,11,12},
									{ 13, 14, 15, 16 } };
		rotate(matrix);
	}
}
