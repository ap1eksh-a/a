import java.io.*;
import java.util.*;

public class macro2 {

    public static void main(String args[]) {
        BufferedReader br, br1, br2;
        OutputStream oo;
        String input = null, input1 = null;
        String tt = null;
        String arg = null;
        String macroTokens = null;
        List<String> mnt = new ArrayList<>(); 
        int macroindex[] = new int[10];
        int mcount = 0, arg_count = 0;
        int middlecount = 0;
        int index = 1;
        int main_enc = 0;

        try {
            br = new BufferedReader(new FileReader("C:\\Users\\Anusha Shetty\\Desktop\\Apeksha\\SE Books\\hci\\input3.txt"));
            br1 = new BufferedReader(new FileReader("C:\\Users\\Anusha Shetty\\Desktop\\Apeksha\\SE Books\\hci\\mnt.java"));
            br2 = new BufferedReader(new FileReader("C:\\Users\\Anusha Shetty\\Desktop\\Apeksha\\SE Books\\hci\\mdt.java"));
            File f = new File("finput.txt");
            PrintWriter p = new PrintWriter(f);

            while ((input = br1.readLine()) != null) {
                StringTokenizer st = new StringTokenizer(input, "\t");
                tt = st.nextToken();
                mnt.add(tt);  // Add to ArrayList
                System.out.println(tt);
            }
            
            while ((input = br.readLine()) != null) {
                StringTokenizer st = new StringTokenizer(input, " ");
                tt = st.nextToken();
                if (tt.equals("START")) {
                    main_enc = 1;
                    p.print("START ");
                    tt = st.nextToken();
                    p.println(tt);
                } else {
                    if (main_enc == 1) {
                        if (input.equals("END")) {
                            main_enc = 0;
                            p.println("END");
                        } else {
                            StringTokenizer t = new StringTokenizer(input, " ");
                            while (t.hasMoreTokens()) {
                                macroTokens = t.nextToken();
                                for (int i = 0; i < mnt.size(); i++) {
                                    if (macroTokens.equals(mnt.get(i))) {
                                        int ff = 0;
                                        while ((input1 = br2.readLine()) != null) {
                                            if (input1.equals(mnt.get(i))) {
                                                ff = 1;
                                                continue;
                                            }
                                            if (input1.equals("MEND")) {
                                                ff = 0;
                                            }
                                            if (ff == 1) {
                                                p.println(input1);
                                            }
                                        }
                                    }
                                }

                                if (!(t.hasMoreTokens()) && mnt.contains(macroTokens)) {
                                    // Handle case when last token is macro
                                } else if (!(t.hasMoreTokens())) {
                                    p.println(macroTokens);
                                } else {
                                    if (mnt.contains(macroTokens)) {
                                        System.out.println("hi");
                                    } else {
                                        p.print(macroTokens + " ");
                                    }
                                }
                            }
                        }
                    }
                }
                index++;
            }
            p.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
