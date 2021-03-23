public class TrafficController {

    private volatile boolean isCarOnBridge = false;

    public synchronized void enterLeft() {
        while (isCarOnBridge) {
            int i = 0;
        }
        isCarOnBridge = true;
    }
    public synchronized void enterRight() {
        while (isCarOnBridge) {
            int i = 0;
        }
        isCarOnBridge = true;
    }
    public void leaveLeft() {
        isCarOnBridge = false;
    }
    public void leaveRight() {
        isCarOnBridge = false;
    }

}