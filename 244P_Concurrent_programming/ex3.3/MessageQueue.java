import java.util.concurrent.LinkedBlockingQueue;
import java.util.ArrayList;
import java.util.Scanner;

public class MessageQueue {
    private static int n_ids;

    public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String input; int produceramt; int consumeramt;

		System.out.println("How many producers would you like to create?");
		input = scanner.nextLine();
		produceramt = Integer.parseInt(input);

		System.out.println("How many consumers would you like to create?");
		input = scanner.nextLine();
		consumeramt = Integer.parseInt(input);

		LinkedBlockingQueue<Message> queue = new LinkedBlockingQueue<>(10);
		ArrayList<Producer> producers = new ArrayList<>();
		for (int i = 0; i < produceramt; i++) producers.add(new Producer(queue, n_ids++));
		ArrayList<Consumer> consumers = new ArrayList<>();
		for (int i = 0; i < consumeramt; i++) consumers.add(new Consumer(queue, n_ids++));

		for (Producer p : producers) new Thread(p).start();
		for (Consumer c : consumers) new Thread(c).start();

		try {
			Thread.sleep(10000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

		for (Producer p : producers) p.stop();
    }
}
