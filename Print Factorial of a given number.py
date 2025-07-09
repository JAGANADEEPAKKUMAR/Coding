#Python

num = int(input())
fact = 1
for i in range(num,0,-1):
    fact *= i
print(fact)

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int fact = 1;
        for(int i = num; i > 0; i--){
            fact *= i;
        }
        System.out.println(fact);
    }
}
