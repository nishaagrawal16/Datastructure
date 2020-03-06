# Find the minimum positive missing number
# Steps:
# ------
# Check 0 < nums < len(arr) and swap that number in their position.
# e.g 3 will be on 2nd position, 4 will be on 3rd position and so on
# Check i+1 != nums[i] 
# O(n)
# TODO

class Solutions:
    def minimum_missing_number(self, nums):
        nums = list(set(nums))
        n = len(nums)
        if n == 0:
            return 1

        i = 0
        while i < n:
            if nums[i] < 1:
                del nums[i]
            else:
                i += 1
            n = len(nums)       
        n = len(nums)
        for i in range(n):
            # Check numbers which are smaller than length of given array
            if nums[i] <= n and nums[i] != i+1:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n + 1

    
    def minimum_missing_number2(self, nums):
        nums = list(set(nums))
        n = len(nums)
        for i in range(n):
            # Check numbers which are smaller than length of given array and greater than zero.
            if 0 < nums[i] <= n:
                # Need to use swap function here
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # print('final: ', nums)
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n + 1

    # def swap(self, A, i):
    #     if not A:
    #         return 1
    #     while 1:
    #         if A[i] == A[A[i]-1]:
    #             break
    #         tmp = A[A[i]-1]
    #         A[A[i]-1] = A[i]
    #         if tmp - 1 == i:
    #             A[i] = tmp
    #             break
    #         elif not (1 <= tmp <= len(A)):
    #             break
    #         else:
    #             A[i] = A[tmp-1]
    #             A[tmp-1] = tmp
    #             if not (1 <= A[i] <= len(A)):
    #                 break

def main():
    nums = [5, 7, 2, 1, 8]
    # nums = [3, 4, -1, 0]
    # nums = [1, 2 ,0]
    # nums = [-1, 4, 2, 1, 9, 10]
    # nums = [-10, -3, -100, -1000, -239, 1]
    # nums = [-1, -2]
    # nums = [2, 2, 4, 0, 1, 3, 3, 3, 4, 3]
    # nums = [699, 0, 0, 9, 0, 0, 0, 0, 1]
    # nums = [3,4,-1,1]
    # nums = [99,94,96,11,92,5,91,89,57,85,66,63,84,81,79,61,74,78,77,30,64,13,58,18,70,69,51,12,32,34,9,43,39,8,1,38,49,27,21,45,47,44,53,52,48,19,50,59,3,40,31,82,23,56,37,41,16,28,22,33,65,42,54,20,29,25,10,26,4,60,67,83,62,71,24,35,72,55,75,0,2,46,15,80,6,36,14,73,76,86,88,7,17,87,68,90,95,93,97,98]
    s = Solutions()
    print(s.minimum_missing_number(nums))
    print(s.minimum_missing_number2(nums))
    # print(s.minimum_missing_number3(nums))

if __name__ == '__main__':
    main()

