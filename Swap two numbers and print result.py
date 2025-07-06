#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println("Before swapping : "+a+" "+b);
        int temp = a;
        a = b;
        b = temp;
        System.out.println("After swapping : "+a+" "+b);
    }
}

#Python

a,b = list(map(int,input().split()))
print("Before swapping :",a,b);
temp = a
a = b
b = temp
print("After swapping :",a,b);
