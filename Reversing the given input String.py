#Python

s = input()
reversed = ""
for i in range(len(s)-1,-1,-1):
    reversed += s[i]
print(reversed)

OR

s = input()
reversed = s[::-1]
print(reversed)

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    String reversed = "";
    for(int i = s.length()-1; i >= 0; i--){
        reversed += s.charAt(i);
       }
    System.out.println(reversed);
    }
}

OR

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String reversed = new StringBuilder(input).reverse().toString();
        System.out.println(reversed);
    }
}
