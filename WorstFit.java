import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class WorstFit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of jobs:");
        int n = sc.nextInt();
        System.out.println("Enter number of blocks:");
        int b = sc.nextInt();
        
        int[] jobs = new int[n];
        Integer[] block = new Integer[b];
        int[] allocation = new int[n];
        int[] flag = new int[b];

        System.out.println("Enter jobs:");
        for (int i = 0; i < n; i++) {
            jobs[i] = sc.nextInt();
        }

        System.out.println("Enter blocks:");
        for (int i = 0; i < b; i++) {
            block[i] = sc.nextInt();
            flag[i] = 0;
        }

        for (int i = 0; i < n; i++) {
            allocation[i] = -1;
        }

        // Sort blocks in descending order for Worst Fit
        Arrays.sort(block, Collections.reverseOrder());

        int memoryUtilized = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < b; j++) {
                if (jobs[i] <= block[j] && flag[j] == 0) {
                    System.out.println(jobs[i] + " job fitted in " + block[j] + " block");
                    flag[j] = 1;
                    memoryUtilized += jobs[i];
                    allocation[i] = j;
                    break;
                }
            }
        }

        System.out.println("Total Memory Utilization: " + memoryUtilized);

        for (int i = 0; i < n; i++) {
            if (allocation[i] == -1) {
                System.out.println("Memory is not allocated for " + i + "th job");
            }
        }
    }
}
