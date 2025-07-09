#Python

numbers = list(map(int,input().split()))
Sum = 0
Sum = sum(numbers)
avg = Sum / 10
print("Sum :",Sum)
print("Average : {:.2f}".format(avg))

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num[] = new int[10];
        int sum = 0;
        for (int i = 0; i < 10; i++) {
            num[i] = sc.nextInt();
            sum += num[i];
        }
        double average = sum / 10.0;
        System.out.println("Sum : " + sum);
        System.out.printf("Average : %.2f\n", average);
    }
}
