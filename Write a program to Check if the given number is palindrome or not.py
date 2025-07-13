#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int temp = num;
        int rev = 0;
        int rem;
        while(num > 0){
            rem = num % 10;
            rev = rev * 10 + rem;
            num = num / 10;
        }
        if(rev == temp){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}

#Python

num = int(input())
rev = 0
temp = num
while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if(rev == temp):
    print("Yes")
else:
    print("No")
