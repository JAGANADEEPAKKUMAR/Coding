#Python

def maximum(a,b):
    if(a > b):
        return a
    else:
        return b
num1,num2 = [int(x) for x in input().split()]
print(maximum(num1,num2))

#Java

import java.io.*;
import java.util.*;

public class Solution {
   public static int Maximum(int a,int b){
       if(a > b){
           return a;
       }
       else{
           return b;
       }
   }
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
       int a = sc.nextInt();
       int b = sc.nextInt();
       int maximum = Maximum(a,b);
        System.out.println(maximum);
    }
}
