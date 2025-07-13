#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int rev = 0;
        int rem;
        int count = 0;
        while(num > 0){
            rem = num % 10;
            rev = rev * 10 + rem;
            num = num / 10;
        }
        for(int i = 1; i < rev + 1; i++){
            if (rev % i == 0){
                count += 1;
            }
        }
        if(count == 2){
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
count = 0
while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
for i in range(1,rev + 1):
    if(rev % i == 0):
        count += 1
if(count == 2):
    print('Yes')
else:
    print('No')
