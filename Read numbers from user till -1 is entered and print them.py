#Python

numbers = list(map(int,input().split()))
for i in numbers:
    if i == -1:
        break
    print(i, end = " ")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<>();
         while (sc.hasNextInt()) {
            int num = sc.nextInt();
            if (num == -1) {
                break;
            }
            numbers.add(num);
        }

        for (int number : numbers) {
            System.out.print(number+" ");
        }

        sc.close();
    
    }
}
