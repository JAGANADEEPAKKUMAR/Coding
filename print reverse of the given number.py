#Python

num = int(input())
rev = 0
while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print(rev)

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rev = 0;
        int rem;
        int num = sc.nextInt();
        while(num > 0){
            rem = num % 10;
            rev = rev * 10 + rem;
            num = num / 10;
        }
        System.out.println(rev);
    }
}
