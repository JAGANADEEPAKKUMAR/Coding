#Python

import ctypes
print("Size of int :", ctypes.sizeof(ctypes.c_int))
print("Size of float :", ctypes.sizeof(ctypes.c_float))
print("Size of char :", ctypes.sizeof(ctypes.c_char))

#Java

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
         System.out.println("Size of int : " + (Integer.SIZE / 8));
        System.out.println("Size of float : " + (Float.SIZE / 8));
        System.out.println("Size of char : " + (Character.SIZE / 16));
    }
}
