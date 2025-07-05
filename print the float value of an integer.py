#Python

num = int(input())
print("{:.2f}".format(float(num)))

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        System.out.printf("%.2f",(float)num);
    }
}
