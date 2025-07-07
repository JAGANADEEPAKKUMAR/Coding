#Python

num = int(input())
for i in range(1, num + 1):
    if(i % 3 == 0):
        print(i,end = " ")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        for(int i = 1; i < num + 1; i++){
            if(i % 3 == 0){
                System.out.print(i + " ");
            }
        }
    }
}
