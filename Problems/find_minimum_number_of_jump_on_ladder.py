# Find the minimum number of jumps which the person needs to travel
# from the starting to end. Here 0 is the safe path and 1 has the problem.
# O(n)

class Solution(object):
    def ladder(self, x):
        n = len(x)
        arr = []
        i = -1
        while i < n:
            if i + 2 < n:
                if x[i+2] == 1:
                    i = i + 1
                else:
                    i = i + 2
            elif i + 1 < n:
                if x[i+1] == 1:
                    return arr
                else:
                    i = i + 1
            else:
                return arr                    
            arr.append(i)
        return arr

def main():  
    s = Solution()
    print(s.ladder([0,1,0,0,0,1,0,0,1]))
    print(s.ladder([0, 0, 0, 0, 1, 0]))
    print(s.ladder([0, 0, 0, 1, 0, 0]))
    print(s.ladder([0, 0, 1, 0, 0, 1, 0]))

if __name__ == '__main__':
    main()

# Output:
# ---------
# [0, 2, 4, 6, 7]
# [1, 3, 5]
# [1, 2, 4, 5]
# [1, 3, 4, 6]
