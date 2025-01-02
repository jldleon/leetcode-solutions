"""
Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k.

Examples:

Input: arr = [10, 2, -2, -20, 10], k = -10
Output: 3
Explaination: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.

Input: arr = [9, 4, 20, 3, 10, 5], k = 33
Output: 2
Explaination: Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.

Input: arr = [1, 3, 5], k = 0
Output: 0
Explaination: No subarray with 0 sum.

Constraints:

    1 ≤ arr.size() ≤ 105
    -103 ≤ arr[i] ≤ 103
    -107 ≤ k ≤ 107

"""

class Solution:
    def countSubarrays(self, arr, k):
        count = 0                   # Contador de subarreglos
        current_sum = 0             # Suma acumulada
        prefix_sums = {0: 1}        # Diccionario con la suma acumulada inicial (caso base)

        for num in arr:             # Iteramos sobre los elementos del arreglo
            current_sum += num      # Actualizamos la suma acumulada
            
            # Verificamos si existe un subarreglo con suma k
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]  # Sumamos las ocurrencias previas

            # Actualizamos el diccionario con la suma acumulada actual
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
        
        return count                # Devolvemos el número total de subarreglos

                
def main():
    arr = [9, 4, 20, 3, 10, 5]
    k = 33

    solution = Solution()

    result = solution.countSubarrays(arr, k)

    print(result)


main()