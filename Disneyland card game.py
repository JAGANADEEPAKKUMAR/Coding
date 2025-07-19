#Python

card_numbers = [int(x) for x in input().split()]
Sum = 0
for num in card_numbers:
    if num != -999:
        Sum += num
print("The credit points :",Sum)

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       String input = sc.nextLine();
       String[] parts = input.split(" ");
        
        int Sum = 0;
        for(String part:parts){
            int num = Integer.parseInt(part);
            if(num != -999){
                Sum += num;
            }
        }
        System.out.println("The credit points : "+Sum);
    }
}
