#Python

a,b = list(map(float,input().split()))
print(f"{(a*b):.2f}")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float a = sc.nextFloat();
        float b = sc.nextFloat();
        System.out.printf("%.2f",(a*b));
    }
}
