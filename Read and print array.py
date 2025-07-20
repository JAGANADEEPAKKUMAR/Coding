#Python

array = [int(x) for x in input().split()]
for num in array:
    print(num,end = ' ')

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     ArrayList<Integer> array = new ArrayList<>();
     while(sc.hasNextInt()){
         array.add(sc.nextInt());
     }   
        for(int num : array){
            System.out.print(num+" ");
        }
    }
}
