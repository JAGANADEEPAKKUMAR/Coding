#Python

sentence = input().split()
for word in sentence:
    if word == "the":
        sentence.remove(word)
        break
print(" ".join(sentence))

#Java

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        
        String[] words = line.split(" ");
        ArrayList<String> sentence = new ArrayList<>(Arrays.asList(words));

        for (int i = 0; i < sentence.size(); i++) {
            if (sentence.get(i).equals("the")) {
                sentence.remove(i);
                break;
            }
        }

        
        for (int i = 0; i < sentence.size(); i++) {
            System.out.print(sentence.get(i));
            if (i != sentence.size() - 1) {
                System.out.print(" ");
            }
        }
    }
}
