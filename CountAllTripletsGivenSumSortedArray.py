"""
Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Two triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2

Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1. 

Constraints:
3 ≤ arr.size() ≤ 103
-105 ≤ arr[i], target ≤ 105

"""

class Solution:
    def countTriplets(self, arr, target):
        # code here
        
        count = 0
        
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if (arr[i] + arr[j] + arr[k] == target):
                        count += 1
        
        return count
    
def main():
    arr = [-3, -1, -1, 0, 1, 2]
    target = -2

    sol = Solution()

    result = sol.countTriplets(arr, target)

    print(result)


main()

    