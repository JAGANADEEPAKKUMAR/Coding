#Python

num = int(input())
for i in range(1,11):
    print(num,"*",i,"=",num*i)

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        for(int i = 1; i < 11; i++){
            System.out.println(num +" " + "*" + " "+ i + " "+ "=" +" " + (num*i));
        }
    }
}
