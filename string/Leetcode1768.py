def mergeAlternately(word1: str, word2: str):
        result = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i += 1
        return result

word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1,word2))
