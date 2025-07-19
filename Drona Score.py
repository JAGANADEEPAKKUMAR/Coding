#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int target = sc.nextInt();
       int Sum = 0;
       int turns = 0;
        while(Sum < target && sc.hasNextInt()){
            int score = sc.nextInt();
            Sum += score;
            turns++;
        }
        System.out.println("The number of turns is "+turns);
        
    }
}

#Python

turns = [int(x) for x in input().split()]
length = len(turns)
print("The number of turns is",length - 1)
