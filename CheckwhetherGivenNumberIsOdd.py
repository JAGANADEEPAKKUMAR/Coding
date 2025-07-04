#Python

num = int(input())
if(num % 2 != 0):
    print("Yes it is odd")
else:
    print("No it is not odd")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        if(num % 2 != 0){
            System.out.println("Yes it is odd");
        }
        else{
             System.out.println("No it is not odd");
        }
    }
}
