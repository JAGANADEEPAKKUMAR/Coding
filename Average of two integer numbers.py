#Python

a,b = list(map(int,input().split()))
print(f"{((a+b)/2):.2f}")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        double avg = (a+b)/2.0;
        System.out.printf("%.2f",avg);
    }
}
