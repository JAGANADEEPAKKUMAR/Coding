#Python

def IsPrime(num):
    count = 0
    for i in range(1, num + 1):
        if(num % i == 0):
            count += 1
    if(count == 2):
        return 1
    else:
        return 0
number = int(input())
print(IsPrime(number))

#Java

import java.io.*;
import java.util.*;

public class Solution {
     public static int IsPrime(int num){
         int count = 0;
         for(int i = 1; i < num + 1; i++){
             if(num % i == 0){
                 count += 1;
             }
         }
         if(count == 2){
             return 1;
         }
         else{
             return 0;
         }
     }
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    int Prime = IsPrime(num);
    System.out.println(Prime);    
    }
}
