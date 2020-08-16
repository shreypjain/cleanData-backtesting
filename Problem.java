import java.util.Random;

public class Problem {
    public static void main(String [] args) {
        int head = 0,tail = 0;
        Random rd = new Random();
        for(int i =0;i<100;i++) {
            boolean coinValue = rd.nextBoolean();
            if(coinValue) {
                head++;
            } else {
                tail++;
            }
        }
        System.out.println("Heads: " + head);
        System.out.println("Tails: " + tail);
    }
}