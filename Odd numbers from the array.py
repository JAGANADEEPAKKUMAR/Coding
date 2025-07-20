#Python

n = int(input())
num = [int(x) for x in input().split()]
odd = []
for i in num:
    if i % 2 != 0:
        odd.append(i)
for x in odd:
    print(x, end=" ")


#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     ArrayList<Integer> nums = new ArrayList<>();
        int n = sc.nextInt();
         for (int i = 0; i < n; i++) {
            nums.add(sc.nextInt());
        }
     for(int num:nums){
         if(num % 2 != 0){
             System.out.print(num+" ");
         }
     }   
    }
}
