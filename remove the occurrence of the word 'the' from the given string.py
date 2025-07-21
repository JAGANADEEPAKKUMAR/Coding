#Python

sentence = input().split()
for word in sentence:
    if word == "the":
        sentence.remove(word)
        break
print(" ".join(sentence))

#Java

