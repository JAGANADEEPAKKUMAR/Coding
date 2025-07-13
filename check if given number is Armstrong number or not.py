#Python

n = int(input())
times = 0
Sum = 0
t = n
p = n
while(t != 0):
    times += 1
    t = t // 10
while(p > 0):
    r = p  % 10
    Sum += (r ** times)
    p = p // 10
if(Sum == n):
    print('Yes')
else:
    print('No')

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int times = 0;
    int Sum = 0;
    int temp = n;
    int p = n;
    int rem;
    while(temp != 0){
        times += 1;
        temp = temp / 10;
    }
    while(p > 0){
        rem = p % 10;
        Sum += (int)Math.pow(rem, times);
        p = p / 10;
    }
    if(Sum == n){
        System.out.println("Yes");
    }
        else{
            System.out.println("No");
        }
    }
}
