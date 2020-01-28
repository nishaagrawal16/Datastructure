# Segregate 0 and 1 in the list in O(n) without using extra space.
# Need to check 0 from the begning and 1 from the end of the list until
# i < j

class Solution(object):
    def seprate_0_1(self, x):
        n = len(x)
        i = 0
        j = n-1
        while(i < j):
            if x[i] == 1:
                if x[j] == 0:
                    x[i], x[j] = x[j], x[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        return x

def main():  
    s = Solution()
    print(s.seprate_0_1([0,1,0,0,0,1,0,0,1]))
    print(s.seprate_0_1([0, 0, 0, 0, 1, 0]))
    print(s.seprate_0_1([0, 0, 0, 1, 0, 0]))
    print(s.seprate_0_1([1, 0, 1, 0, 1, 1, 0]))


if __name__ == '__main__':
    main()

# Output:
# -------
# [0, 0, 0, 0, 0, 0, 1, 1, 1]
# [0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 1]
# [0, 0, 0, 1, 1, 1, 1]
