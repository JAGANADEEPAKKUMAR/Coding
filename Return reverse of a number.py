#Python

def Reverse(num):
    rev = 0
    while(num > 0):
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev
num = int(input())
print(Reverse(num)) 

#Java

import java.io.*;
import java.util.*;

public class Solution {
   public static int Reverse(int num){
       int rem;
       int rev = 0;
       while(num > 0){
           rem = num % 10;
           rev = rev * 10 + rem;
           num = num / 10;
       }
       return rev;
   }
    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     int num = sc.nextInt();
     int reverse = Reverse(num);
     System.out.println(reverse);   
   }
}
