import java.util.Scanner;

public class Nextfit {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of jobs :");
        int n = sc.nextInt();
        System.out.println("Enter number of blocks :");
        int b = sc.nextInt();

        int[] jobs = new int[n];
        int[] block = new int[b];
        int[] allocation = new int[n];
        int[] flag = new int[b];

        System.out.println("Enter jobs :");
        for (int i = 0; i < n; i++) {
            jobs[i] = sc.nextInt();
        }
        System.out.println("Enter blocks :");
        for (int i = 0; i < b; i++) {
            block[i] = sc.nextInt();
            flag[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            allocation[i] = -1;
        }
        int memoryUtilized = 0;
        int pointer = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = pointer; j < b; j++) {
                if (jobs[i] <= block[j] && flag[j] == 0) {
                    System.out.println(jobs[i] + " job fitted in " + block[j] + " block");
                    allocation[i] = j;
                    flag[j] = 1;
                    memoryUtilized += jobs[i];
                    if (j != b - 1) {
                        pointer = j + 1;
                    } else{
                        pointer = 0;
                    }
                    break;
                }
            }
        }
        System.out.println("Total Memory Utilization: " + memoryUtilized);
        for (int i = 0; i < n; i++) {
            if (allocation[i] == -1) {
                System.out.println("Memory is not allocated for " + jobs[i] + " job");
            }
        }
    }
}
