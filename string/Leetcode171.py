def titleToNumber(col: str):
        num = 0
        for c in col:
          num = num * 26 + (ord(c) - ord('A') + 1)
        return num

print(titleToNumber("ZY"))

