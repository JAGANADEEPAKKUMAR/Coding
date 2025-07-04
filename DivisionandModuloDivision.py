#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        int d = sc.nextInt();
        int division = c / d;
        int modulo_division = c % d;
        System.out.println("Result of division is : "+division);
        System.out.println("Result of modulo division is : "+modulo_division);
    }
}

#Python

c,d = list(map(int,input().split()))
division = c // d
modulo_division = c % d
print("Result of division is :",division)
print("Result of modulo division is :",modulo_division)
