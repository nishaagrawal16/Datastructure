# Maximum value of |arr[i] – arr[j]| + |i – j|
# https://www.geeksforgeeks.org/maximum-value-arri-arrj-j/
# We can break this expression and create the following equations:
# (arr[i] + i) - (arr[j] + j)
# (arr[i] - i) - (arr[j] - j)
# Find the max from the both
# O(n)

class Solutions:
    def find_max(self, arr):
        # min1 is for `(arr[i] + i)` and min2 is for `(arr[i] - i)`
        min1 = max1 = min2 = max2 = arr[0]
        i = 1
        while i < len(arr):
            # For getting the min and max in arr[i] + i
            if arr[i] + i < min1:
                min1 = arr[i] + i

            if arr[i] + i > max1:
                max1 = arr[i] + i

            # For getting the min and max in arr[i] - i
            if arr[i] - i < min2:
                min2 = arr[i] - i

            if arr[i] - i > max2:
                max2 = arr[i] - i
            i += 1
        a1 = max1 - min1
        a2 = max2 - min2
        print(a1, a2)
        if a1 > a2:
            print('Max: ', a1)
        else:
            print('Max: ', a2)

def main():
    # arr = [1, 2, 3, 1]
    arr = [10, 5, 0]
    print('Array: ', arr)
    s = Solutions()
    s.find_max(arr)

if __name__ == '__main__':
    main()

# Output:
# -------
# Array:  [10, 5, 0]
# 8 12
# Max:  12
