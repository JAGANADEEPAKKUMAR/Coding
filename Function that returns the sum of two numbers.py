#Python

def add(a,b):
    return a + b
num1,num2 = list(map(int,input().split()))

answer = add(num1,num2)
print(answer)

#Java

import java.io.*;
import java.util.*;

public class Sum {
    public static int add(int a,int b){
        return a + b;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int answer = add(num1,num2);
        System.out.println(answer);
    }
}
