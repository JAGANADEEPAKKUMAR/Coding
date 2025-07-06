#Python

vowels = ['a','e','i','o','u','A','E','I','O','U']
letter = input()
if letter in vowels:
    print("Vowel")
else:
    print("Consonant")

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char c = sc.nextLine().charAt(0);
        if(c == 'A' || c == 'E' || c == 'I'|| c == 'O'|| c == 'U'|| c == 'a'|| c == 'e'|| c == 'i'|| c == 'o'|| c == 'u'){
            System.out.println("Vowel");
        }
        else{
            System.out.println("Consonant");
        }
    }
}
