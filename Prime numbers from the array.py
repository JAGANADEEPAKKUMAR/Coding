#Python

def is_prime(num):
    if n <= 1:
        return False
    else:
        count = 0
        for i in range(1, num + 1):
            if(num % i == 0):
                count += 1
            
    return count == 2
num = int(input())
nums = list(map(int,input().split()))

prime = []
for n in nums:
    if is_prime(n):
        prime.append(n)
if not prime:
    print(-1)
else:
    print(*prime)
  
#Java

import java.io.*;
import java.util.*;

public class Solution {
    static ArrayList<Integer> prime = new ArrayList<>();
     public static void CheckPrime(int n){
         int count = 0;
         for(int i = 1; i <= n; i++){
             if(n % i == 0){
                 count += 1;
             }
         }
        if(count == 2){
            prime.add(n);
        }
}
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    ArrayList<Integer> nums = new ArrayList<>();
    for(int i = 0; i < num; i++){
        nums.add(sc.nextInt());
    }
        for(int i = 0; i < nums.size(); i++){
            CheckPrime(nums.get(i));
        }
         if (prime.isEmpty()) {
            System.out.println("-1");
        } else {
            for (int p : prime) {
                System.out.print(p + " ");
    }
}
    }
}
