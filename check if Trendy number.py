#Python

num = int(input())
count = 0
while(num > 0):
    rem = num % 10
    count += 1
    if(count == 2):
        middle = rem
    num =  num // 10
if(count == 3 and middle % 3 == 0):
    print("Trendy")
else:
    print("Not trendy")
  
#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int count = 0;
        int rem;
        int middle = 0;
        while(num > 0){
            rem = num % 10;
            count += 1;
            if(count == 2){
                middle = rem;
            }
            num = num / 10;
        }
    if (count == 3 && middle % 3 == 0){
        System.out.println("Trendy");
    }
        else{
            System.out.println("Not trendy");
}
        
    }
}
