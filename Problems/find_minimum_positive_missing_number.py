# TO DO

class Solutions:
    def minimum_missing_number(self, nums):
        n = len(nums)
        if n == 0:
            return 1
        # for i in range(n):
        #     # Check numbers which are smaller than length of given array
        #     # and greater that 0.
        #     if nums[i] <= n and nums[i] > 0:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # print('nums: ', nums)
        # for i in range(len(nums)):
        #     if nums[i] < 1:
        #         del nums[i]
        #     if  i < len(nums) and i+1 != nums[i]:
        #         return i+1
        # return len(nums) + 1

        for i in range(len(nums)):
            print(i, nums)
            if i == len(nums) - 1:
                break
            if nums[i] < 1:
                del nums[i]

        n = len(nums)
        for i in range(n):
            print('inside: ', i, nums)
            # Check numbers which are smaller than length of given array
            if nums[i] <= n and nums[i] != i+1:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            print('final nums: ', nums)
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n + 1


def main():
    # nums = [5, 7, 2, 1, 8]
    # nums = [3, 4, -1, 0]
    # nums = [1, 2 ,0]
    nums = [-1,4,2,1,9,10]
    s = Solutions()
    print(s.minimum_missing_number(nums))

if __name__ == '__main__':
    main()

