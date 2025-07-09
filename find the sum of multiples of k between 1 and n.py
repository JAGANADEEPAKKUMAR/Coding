#Python

k = int(input())
n = int(input())
multiples = n // k
Sum = 0
for i in range(1,multiples + 1):
    Sum += (k*i)
print(Sum)

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int n = sc.nextInt();
        int multiples = n / k;
        int sum = 0;
        for(int i = 1; i <= multiples; i++){
            sum += (k*i);
        }    
        System.out.println(sum);
    }
   
    
}
