#Python

n = int(input())
nums = list(map(int,input().split()))
print(max(nums))

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    ArrayList<Integer> nums = new ArrayList<>();
    for(int i = 0; i < num; i++){
        nums.add(sc.nextInt());
    }
     int max = nums.get(0);
     for(int i = 1; i < nums.size(); i++){
         if(nums.get(i) > max){
             max = nums.get(i);
         }
     }
        System.out.println(max);
    }
}


OR

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    ArrayList<Integer> nums = new ArrayList<>();
    for(int i = 0; i < num; i++){
        nums.add(sc.nextInt());
    }
     int max = Collections.max(nums);
    System.out.println(max);
    }
}
