package dp;

public class KSmallest {

	private static int ksmallest(int[] A, int sizeA, int[] B, int sizeB, int k) {

		// Lower bound of elements we will choose in A.
		int b = Math.max(0, k - sizeB);
		// Upper bound of elements we will choose in A.
		int t = Math.min(sizeA, k);

		while (b < t) {
			int x = b + ((t - b) / 2);
			int ax1 = (x <= 0 ? Integer.MIN_VALUE : A[x - 1]);
			int ax = (x >= sizeA ? Integer.MAX_VALUE : A[x]);
			int bkx1 = (k - x <= 0 ? Integer.MIN_VALUE : B[k - x - 1]);
			int bkx = (k - x >= sizeB ? Integer.MAX_VALUE : B[k - x]);

			if (ax < bkx1) {
				b = x + 1;
			} else if (ax1 > bkx) {
				t = x - 1;
			} else {
				// B.get(k - x - 1) <= A.get(x) && A.get(x - 1) < B.get(k - x).
				return Math.max(ax1, bkx1);
			}
		}

		int ab1 = b <= 0 ? Integer.MIN_VALUE : A[b - 1];
		int bkb1 = k - b - 1 < 0 ? Integer.MIN_VALUE : B[k - b - 1];
		return Math.max(ab1, bkb1);
	}

	double findMedian(int A[], int B[], int l, int r, int nA, int nB) {
		if (l > r)
			return findMedian(B, A, Math.max(0, (nA + nB) / 2 - nA), Math.min(nB, (nA + nB) / 2), nB, nA);
		int i = (l + r) / 2;
		int j = (nA + nB) / 2 - i - 1;
		if (j >= 0 && A[i] < B[j])
			return findMedian(A, B, i + 1, r, nA, nB);
		else if (j < nB - 1 && A[i] > B[j + 1])
			return findMedian(A, B, l, i - 1, nA, nB);
		else {
			if ((nA + nB) % 2 == 1)
				return A[i];
			else if (i > 0)
				return (A[i] + Math.max(B[j], A[i - 1])) / 2.0;
			else
				return (A[i] + B[j]) / 2.0;
		}
	}

	double findMedianSortedArrays(int A[], int n, int B[], int m) {
		if (n < m)
			return findMedian(A, B, 0, n - 1, n, m);
		else
			return findMedian(B, A, 0, m - 1, m, n);
	}

	public static void main(String[] args) {
		int[] a = { 1, 2, 3, 4, 5 };
		int[] b = { 6, 7, 8, 9, 12 };
		System.out.println(ksmallest(a, a.length, b, b.length, 6));
	}

}
