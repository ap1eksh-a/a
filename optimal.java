import java.util.*;

public class optimal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter length of ref string:");
        int n = sc.nextInt();
        
        System.out.println("Enter number of frames:");
        int frames = sc.nextInt();
        
        int rs[] = new int[n];            // Reference string
        int buffer[] = new int[frames];   // Frame buffer
        int ind[] = new int[frames];      // To track future use
        int m_layout[][] = new int[n][frames]; // For displaying memory layout
        
        int hit = 0, fault = 0, pointer = 0;
        int search, maxind;
        
        System.out.println("Enter ref string:");
        for (int i = 0; i < n; i++) {
            rs[i] = sc.nextInt();
        }
         
        // Initialize buffer and ind arrays
        for (int j = 0; j < frames; j++) {
            buffer[j] = -1;
            ind[j] = -1;
        }
         
        // Main loop for processing the reference string
        for (int i = 0; i < n; i++) {
            search = -1;

            // Check if the current page is already in buffer (hit)
            for (int j = 0; j < frames; j++) {
                if (buffer[j] == rs[i]) {
                    search = j;
                    hit++;
                    break;
                }
            }

            // Page fault case
            if (search == -1) {
                fault++;

                // If there's an empty frame, use it
                if (buffer[pointer] == -1) {
                    buffer[pointer] = rs[i];
                    pointer++;
                    if (pointer == frames) {
                        pointer = 0; // reset pointer if it reaches frame limit
                    }
                } else {
                    // Otherwise, use the optimal replacement policy
                    maxind = -1;
                    int replaceIndex = -1; // Track which frame to replace

                    // Check future uses for all pages in buffer
                    for (int k = 0; k < frames; k++) {
                        ind[k] = -1; // Reset future use index
                        for (int j = i + 1; j < n; j++) {
                            if (buffer[k] == rs[j]) {
                                ind[k] = j; // Store the index of next use
                                break;
                            }
                        }
                        if (ind[k] == -1) {
                            ind[k] = 99; // If not used again, set to a large value
                        }

                        // Find the page with the furthest future use
                        if (ind[k] > maxind) {
                            maxind = ind[k];
                            replaceIndex = k;
                        }
                    }

                    // Replace the page
                    buffer[replaceIndex] = rs[i];
                }
            }

            // Store the current state of the buffer for memory layout display
            for (int j = 0; j < frames; j++) {
                m_layout[i][j] = buffer[j];
            }
        }

        // Print memory layout
        System.out.println("Memory layout:");
        for (int j = 0; j < frames; j++) {
            for (int i = 0; i < n; i++) {
                if (m_layout[i][j] == -1) {
                    System.out.print(" - ");
                } else {
                    System.out.print(" " + m_layout[i][j] + " ");
                }
            }
            System.out.println();
        }

        // Print total hits and faults
        System.out.println("Total hits: " + hit);
        System.out.println("Total faults: " + fault);
    }
}
