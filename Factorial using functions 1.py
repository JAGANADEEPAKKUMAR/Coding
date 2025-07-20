#Python

def Factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
num = int(input())
Fact = Factorial(num)
print("Factorial of",num,":",Fact);

#Java

import java.io.*;
import java.util.*;

public class Solution {
     public static int Factorial(int num){
         int fact = 1;
         for(int i = 1; i < num + 1; i++){
             fact *= i;
         }
         return fact;
     }
    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     int number = sc.nextInt();
     int Fact = Factorial(number);
     System.out.println("Factorial of "+number+" : "+Fact);   
    }
}
