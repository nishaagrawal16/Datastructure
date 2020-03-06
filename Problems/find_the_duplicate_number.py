# Find duplicate number
# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
# O(n)

class Solutions:
    def printRepeating(self, nums):
        if len(nums) == 0:
            return
        for i in range(len(nums)):
            if nums[abs(nums[i])] >= 0:
                nums[abs(nums[i])] = -nums[abs(nums[i])] 
            else: 
                return abs(nums[i])

def main():
    # nums = [3, 1, 3, 4, 2]
    nums = [1, 3, 4, 2, 2]
    s = Solutions() 
    print(s.printRepeating(nums))
  
if __name__ == '__main__':
    main()
