#Python

a,b = list(map(int,input().split()))
if(a>b):
    print(b)
else:
    print(a)
#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        if(a > b){
            System.out.println(b);
        }
        else{
            System.out.println(a);
        }
    }
}
