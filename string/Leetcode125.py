def validP(string):
    s = string.lower()
    first = 0
    last = len(s) - 1

    while first < last:
        if not ('a' <= s[first] <= 'z' or '0' <= s[first] <= '9'):
            first += 1
        elif not ('a' <= s[last] <= 'z' or '0' <= s[last] <= '9'):
            last -= 1
        elif s[first] != s[last]:
            return False
        else:
            first += 1
            last -= 1

    return True


print(validP("race a car"))
