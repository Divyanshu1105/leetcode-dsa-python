def maxNumberOfBalloons(text):
        arr_count = [0] * 26
        for ch in text:
            arr_count[ord(ch) - ord('a')] += 1
        return min(
            arr_count[ord('b') - ord('a')], 
            arr_count[ord('a') - ord('a')],    
            arr_count[ord('l') - ord('a')] // 2,  
            arr_count[ord('o') - ord('a')] // 2,
            arr_count[ord('n') - ord('a')]  
        )
            


text = "loonbalxballpoon"
print(maxNumberOfBalloons(text))