# Given a collection of intervals, merge all overlapping intervals.
# Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]] 
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# O(n)

class Solutions:
    def overlapping(self, intervals):
        j = 0
        while j < len(intervals) - 1:
            if intervals[j][1] >= intervals[j+1][0]:
                flag = 1
                new_elem = [intervals[j][0], intervals[j+1][1]]
                del intervals[j]
                del intervals[j]
                intervals.insert(j, new_elem)
            else:
                j += 1

        return intervals

def main():
    s = Solutions()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = s.overlapping(intervals)
    print('final intervals: ', intervals)

if __name__ == '__main__':
  main()

