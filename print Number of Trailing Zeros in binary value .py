#Python

num = int(input())
binary = bin(num)[2:]
trailing_zeros = len(binary) - len(binary.rstrip('0'))
print("There are",trailing_zeros,"Trailing Zeros")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    int count = 0;
     if(num == 0){
         System.out.println(0);
     }   
        else{
            while(num % 2 == 0){
                count += 1;
                num /= 2;
            }
    System.out.println("There are "+count+" Trailing Zeros");
        }
    }
}
