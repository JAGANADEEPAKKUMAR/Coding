#Python

op,a,b = input().split()
num1 = int(a)
num2 = int(b)
match op:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        print(num1 / num2)
    case '%':
        print(num1 % num2)
    case _:
        print("Invalid operation")
    
#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       char oper = sc.next().charAt(0);
       int a = sc.nextInt();
       int b = sc.nextInt();
       switch(oper) {
  case '+':
    System.out.println(a+b);
    break;
  case '-':
    System.out.println(a-b);
    break;
   case '*':
    System.out.println(a*b);
    break;
    case '/':
    System.out.println(a/b);
    break;
    case '%':
    System.out.println(a%b);
    break;
  default:
     System.out.println("Invalid operation");
  
} 
    }
}
