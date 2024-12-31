"""
Print Anagrams Together
Difficulty: MediumAccuracy: 65.78%Submissions: 69K+Points: 4

Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

Note: The final output will be in lexicographic order.

Examples:

Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.

Input: arr[] = ["no", "on", "is"]
Output: [["is"], ["no", "on"]]
Explanation: There are 2 groups of anagrams "is" makes group 1. "no", "on" make group 2.

Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]
Explanation: 
Group 1: "abc", "bac", and "cab" are anagrams.
Group 2: "listen", "silent", and "enlist" are anagrams.
Group 3: "rat", "tar", and "art" are anagrams.

Constraints:
1<= arr.size() <=100
1<= arr[i].size() <=10


"""

class Solution:
    
    def is_anagram(word1, word2):
        word1 =  sorted(word1)
        word2 = sorted(word2)

        if word1 == word2:
            return True
        else:
            return False

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
    
        #code here

        n =  len(arr)
        anagrams = [[]*n]
        anagrams[0].append(arr[0])

        print(anagrams)

        i = 1

        while(i < n):
            for ana in anagrams:
                
        




def main():
    arr = ["act", "god", "cat", "dog", "tac"]
    
    print(arr)

    n =  len(arr)
    anagrams = [[]*n]
    print(anagrams)
    anagrams[0].append(arr[0])

    print(anagrams)
    

main()