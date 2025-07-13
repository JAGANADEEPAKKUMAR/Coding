#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Sum = 0;
        ArrayList<Integer> nums = new ArrayList<>();
        while(sc.hasNextInt()){
            int num = sc.nextInt();
            if(num == -1){
                break;
            }
            nums.add(num);
        }
        for(int num: nums){
            Sum += num;
        }
        System.out.println(Sum);
    }
}

# Python

numbers = list(map(int,input().split()))
valid = []
for i in numbers:
    if i == -1:
        break
    valid.append(i)
print(sum(valid))
