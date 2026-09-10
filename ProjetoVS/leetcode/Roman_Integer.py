def romanToInt(self, s='III'):
    hash_roman = {
        'I': 1, 'V': 5,'X': 10, 'L': 50,
        'C': 100,'D': 500,'M': 1000
        }
    result = prev = 0
    for i in range(len(s)):
        curr = hash_roman[i]
        if prev > curr:
            result -= curr
        else:
            result += curr
        prev = curr
    return result

# a1 = romanToInt('III')
# a2 = romanToInt('LVIII')
# a3 = romanToInt('MCMXCIV')

