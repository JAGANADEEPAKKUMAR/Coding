#Python

a,b = list(map(int,input().split()))
if(a % 2 != 0 and b % 2 != 0):
    print("Yes")
else:
    print("No")


#Java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        if(a % 2 != 0 && b % 2 != 0){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
