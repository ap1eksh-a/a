import java.util.Scanner;

public class Firstfit {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of jobs :");
        int n = sc.nextInt();

        System.out.println("Enter number of blocks :");
        int b = sc.nextInt();

        int[] jobs = new int[n];
        int[] blocks = new int[b];
        int[] allocation = new int[n];
        int[] flag = new int[b];

        System.out.println("Enter jobs :");
        for (int i = 0; i < n; i++) {
            jobs[i] = sc.nextInt();
            allocation[i] = -1;
        }

        System.out.println("Enter blocks :");
        for (int i = 0; i < b; i++) {
            blocks[i] = sc.nextInt();
            flag[i] = 0; 
        }

        int memoryUtilized = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < b; j++) {
                if (jobs[i] <= blocks[j] && flag[j] == 0) {
                    System.out.println("Job " + jobs[i] + " is allocated to Block " + blocks[j]);
                    allocation[i] = j; 
                    memoryUtilized += jobs[i];
                    flag[j] = 1; 
                    break; 
                }
            }
        }
        System.out.println("Total Memory Utilization: " + memoryUtilized);

        // Check for unallocated jobs
        for (int i = 0; i < n; i++) {
            if (allocation[i] == -1) {
                System.out.println("Memory is not allocated for job " + jobs[i]);
            }
        }

        sc.close(); // Close the scanner
    }
}
