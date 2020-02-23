# Date: 23-01-2020
# https://www.geeksforgeeks.org/print-longest-substring-without-repeating-characters/
# find and print longest substring without repeating characters.
# O(n)  

class Solution(object):
    def find_longest_unique_string(self, given_str):
        st = 0
        max_length = 0
        curr_len = 0
        start = 0
        pos = {}
        if not len(given_str): # String is empty
            return 0
        elif len(given_str) == 1:
            return given_str[0]
        pos[given_str[0]] = 0
        for i in range(1, len(given_str)):
            if given_str[i] not in pos:
                pos[given_str[i]] = i
            else:
                # Check that repeated value's position is greater than or equal
                # to starting point.
                if pos[given_str[i]] >= st:
                    curr_len = i - st
                    if max_length < curr_len:
                        max_length = curr_len
                        start = st
                    # Next substring will start after the last occurrence of
                    # current character to avoid its repetition.  
                    st = pos[given_str[i]] + 1
            # Update last occurrence of current character.  
            pos[given_str[i]] = i
    
        # Compare length of last substring with max_length  
        # and update max_length and start accordingly.
        if max_length <= i - st:
            max_length = i - st + 1 # Need to increment by one for taking the
            # last element h in "abcabcdefabefabcdefgh"
            start = st
        return given_str[start : start + max_length]     
     

def main():
    str1 = "abaabcdefgh"
    s = Solution()
    longest_str = s.find_longest_unique_string(str1)
    print(longest_str)

if __name__ == '__main__':
    main()
    