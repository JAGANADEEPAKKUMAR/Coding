#Python

num = int(input())
count = 0
for i in range(1, num + 1):
    if (num % i == 0):
        count += 1
if(count == 2):
    print("Yes")
else:
    print("No")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int count = 0;
        for(int i = 1; i < num + 1; i++){
            if(num % i == 0){
                count += 1;
            }
        
        }
        if(count == 2){
            System.out.println("Yes");
        }
            else{
                System.out.println("No");
            }
    }
}
