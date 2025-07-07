#Python

num = int(input())
for i in range(num,0,-1):
    if(i % 2 != 0):
        print(i,end = " ")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        for(int i = num; i > 0; i--){
            if(i % 2 != 0){
            System.out.print(i+" ");
            }
        }
    }
}
