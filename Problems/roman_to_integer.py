class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        switcher = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        switcherSubs = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        i = 0
        result = 0
        while i < len(s):
            values = switcherSubs.get(s[i:i+2], None)
            if values:
                result += values
                i += 2
            else:
                result += switcher.get(s[i])
                i += 1
        return result

s = Solution()
print('*************** ROMAN TO INTEGER ***************')
print('MCMXCIV')
print(s.romanToInt('MCMXCIV'))

# Output:
# -------
# *************** ROMAN TO INTEGER ***************
# MCMXCIV
# 1994
