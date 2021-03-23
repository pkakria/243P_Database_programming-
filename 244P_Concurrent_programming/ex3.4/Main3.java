import java.util.concurrent.*;

public class Main3 {

   private static void nap(int millisecs) {
        try {
            Thread.sleep(millisecs);
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

    private static void addProc(HighLevelDisplay d, Semaphore permit) {

	// Add a sequence of addRow operations with short random naps.
        for (int i = 0; i < 20; i++) {
            try {
                permit.acquire();
                d.addRow("AAAAAAAAAAAA  " + i);
                permit.release();
                nap((int) (Math.random() * 4000));
                permit.acquire();
                d.addRow("BBBBBBBBBBBB  " + i);
                permit.release();
                nap((int) (Math.random() * 4000));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

   }

    private static void deleteProc(HighLevelDisplay d, Semaphore permit) {
	
	// Add a sequence of deletions of row 0 with short random naps.
        for (int i = 0; i < 40; i++) {
            try {
                nap((int) (Math.random() * 5000) + 2000);
                permit.acquire();
                d.deleteRow(0);
                permit.release();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String [] args) {
        final HighLevelDisplay d = new JDisplay2();
        Semaphore permit = new Semaphore(1, true);

        new Thread () {
            public void run() {
                addProc(d, permit);
            }
        }.start();


        new Thread () {
            public void run() {
                deleteProc(d, permit);
            }
        }.start();

    }
}