# Maximum value of |arr[i] – arr[j]| + |i – j|
# https://www.geeksforgeeks.org/maximum-value-arri-arrj-j/
# We can break this expression and create the following equations:
# (arr[i] + i) - (arr[j] + j)
# (arr[i] - i) - (arr[j] - j)
# Find the max from the both
# O(n)

class Solutions:
    def find_max(self, arr):
        min1 = arr[0] # for (arr[i] + i)
        max1 = arr[0]
        min2 = arr[0] # for (arr[i] - i)
        max2 = arr[0]
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
    s = Solutions()
    s.find_max(arr)

if __name__ == '__main__':
    main()
