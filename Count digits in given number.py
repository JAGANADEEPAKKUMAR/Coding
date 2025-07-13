#Python

num = int(input())
count = 0
while(num > 0):
    rem = num % 10
    count += 1
    num = num // 10
print(count)

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     int num = sc.nextInt();
     int count = 0;
     int rem;
     while(num > 0){
         rem = num % 10;
         count += 1;
         num = num / 10;
     }
    System.out.println(count);
    }
}
