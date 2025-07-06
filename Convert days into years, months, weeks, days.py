#Python

days = int(input())
years = days // 365
no_of_months = days % 365
months = no_of_months // 30
no_of_weeks = no_of_months % 30
weeks = no_of_weeks // 7
no_of_days = no_of_weeks % 7
print(years,"year(s)",months,"month(s)",weeks,"week(s)",no_of_days,"day(s)")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int days = sc.nextInt();
        int years = days / 365;
        int no_of_months = days % 365;
        int months = no_of_months / 30;
        int no_of_weeks = no_of_months % 30;
        int weeks = no_of_weeks / 7;
        int no_of_days = no_of_weeks % 7;
        System.out.println(years+" year(s) "+months+" month(s) "+weeks+" week(s) "+no_of_days+" day(s) ");
    }
}
