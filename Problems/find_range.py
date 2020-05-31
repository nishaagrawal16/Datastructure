# Date: 31-May-2020
# Find given range of a number is present in list or not 
# if num = 3 means range [3, 2, 1] should be present in the list 
# O(n)

def findRange(arr, num):
    if not len(arr):
        return False
    num1 = num
    for i in range(len(arr)):
        result = []
        if arr[i] == num:
            num = num - 1
            if arr[i] == 1:
                return True
        else:
            num = num1
    return False

def main():
    # arr = [2, 4, 3, 2, 1, 4, 13, 22, 1]
    arr = [1, 2, 3, 5, 5, 4, 3, 2, 9, 0, 3, 4, 5]
    num = 3
    print(findRange(arr, num))

if __name__ == '__main__':
    main()
