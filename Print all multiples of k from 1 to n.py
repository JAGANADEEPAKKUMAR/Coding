#Python

k = int(input())
n = int(input())
multiples = n // k
for i in range(1,multiples + 1):
    print(k*i, end = " ")
  
#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int n = sc.nextInt();
        int multiples = n / k;
        for(int i = 1; i <= multiples; i++){
            System.out.print((k*i) + " ");
        }    
    }
   
    
}
