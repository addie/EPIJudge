package dp;

import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class DataStream {

	public void calculate(Queue<Double> list1, Queue<Double> list2, double value) {
		list1.offer(value);
		
		//while (!list2.isEmpty()) {
			while (!list2.isEmpty() && (value - list2.peek()) >= 1d) {
				//System.out.println("removing " + list2.poll() + " against " + value);
				list2.poll();
			}

			for (double l2val : list2) {
				if (Math.abs(l2val - value) < 1d) {
					System.out.println(l2val + " ," + value);
				} else {
					break;
				}
			}
		//}
	}

	public class StreamThread extends Thread {

		private Iterator<Double> stream;
		private Queue<Double> q1;
		private Queue<Double> q2;
		private Lock lock;

		public StreamThread(Iterator<Double> stream, Lock lock, Queue<Double> q1, Queue<Double> q2) {
			this.stream = stream;
			this.q1 = q1;
			this.q2 = q2;
			this.lock = lock;
		}

		@Override
		public void run() {

			while (stream.hasNext()) {				
				double value = stream.next();												
				lock.lock();
			//	System.out.println(Thread.currentThread().getName() + " -> " + value);
				calculate(q1, q2, value);
				lock.unlock();
			}
			
		//	System.out.println(Thread.currentThread().getName() + " exit");
		}
	}

	public static void main(String[] args) {

		DataStream s = new DataStream();

		List<Double> stream1 = Arrays.asList(0.2,1.1,1.2,1.3, 1.4,1.5,1.6,1.7,1.8,1.9, 3.0);
		List<Double> stream2 = Arrays.asList(2.0,2.06,2.07, 2.1,2.2,2.4, 4.5);

		Lock lock = new ReentrantLock();
		Queue<Double> q1 = new LinkedList<>();
		Queue<Double> q2 = new LinkedList<>();

		Thread t1 = s.new StreamThread(stream1.iterator(), lock, q1, q2);
		Thread t2 = s.new StreamThread(stream2.iterator(), lock, q2, q1);

		t1.start();
		t2.start();

		try {
			t1.join();
			t2.join();
		} catch (Exception e) {
		}
	}

}
