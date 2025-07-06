#Python

n = int(input())
even = []
for num in range(1,n+1):
    if(num % 2 == 0):
        even.append(num)
for i in even:
    print(i,end = " ")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 1; i < n + 1; i++){
            if( i % 2 == 0){
                System.out.print(i+" ");
            }
        }
    }
}
