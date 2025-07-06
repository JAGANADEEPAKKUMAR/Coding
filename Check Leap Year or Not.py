#Python

year = int(input())
if(year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
    print('Leap year')
else:
    print("Not Leap year")


#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        if(year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)){
            System.out.println("Leap year");
        }
        else{
            System.out.println("Not Leap year");
        }
    }
}
