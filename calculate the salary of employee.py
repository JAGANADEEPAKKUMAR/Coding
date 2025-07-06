#Python

emp_id = int(input())
work_hrs = int(input())
amount = float(input())
salary = work_hrs * amount
print(f"employee id is {emp_id} - salary is {salary:.2f}")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int emp_id = sc.nextInt();
        int work_hrs = sc.nextInt();
        float amount = sc.nextFloat();
        double salary = work_hrs * amount;
        System.out.printf("employee id is "+emp_id+" - "+"salary is "+"%.2f",salary);
    }
}
