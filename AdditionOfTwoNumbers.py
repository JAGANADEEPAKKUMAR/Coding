#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c=a+b;
        System.out.println("The sum of given 2 numbers is : "+c);
    }
}

#Python

a,b = list(map(int,input().split()))
print("The sum of given 2 numbers is :",(a+b))
