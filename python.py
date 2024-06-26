'''
leetcode: https://leetcode.com/problems/two-sum/
hackerrank: ?

Problem: Two Sum

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
'''

def twoSum(nums, target):
        m = {}
        output = []
        
        for i, num in enumerate(nums):
            lookup = target - num            
            if lookup in m:                                
                return [i, m[lookup]]
                
            m.update({ num: i})
                        
        return []
        
        
assert twoSum([2,7,11,15], 9) == [1, 0]
assert twoSum( [3,2,4], 6) == [2,1]

'''
Leetcode: ?
hackerrank: ?

Problem: Flat Array

Example 1:
Input: [1, 2 , 3, [4, 5, 6], 7, 8]
Output: [1, 2 , 3, 4, 5, 6, 7, 8]

Example 2:
Input: [1,2,3,4,[5,6,7,8,9,[10,11,12]],13,14]
Output: [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
'''

def flat(arr):
    output = []
    for index in range(0, len(arr)):
        if isinstance(arr[index], list):
            output.extend(flat(arr[index]))
        else:
            output.append(arr[index])
    return output

assert flat([1, 2 , 3, [4, 5, 6], 7, 8]) == [1, 2 , 3, 4, 5, 6, 7, 8]
assert flat([1,2,3,4,[5,6,7,8,9,[10,11,12]],13,14]) == [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
  

'''
Leetcode: ?
hackerrank: ?

Problem: Flat dictionary

Example 1:
Input: { 'a': 1, 'b': 'foo', 'c': { 'a': 2, 'b': { 'x' : 'zooo', 'z' : 'tooo' } } }
Output: {'a': 1, 'b': 'foo', 'c_a': 2, 'c_b_x': 'zooo', 'c_b_z': 'tooo'}
'''

def flat_concat(key, dictionary):
    dic = {}
    for dic_key in dictionary:
        
        if isinstance(dictionary[dic_key], dict):
            dic.update(flat_concat(key + "_" + dic_key, dictionary[dic_key]))
        else:
            k = key + "_" + dic_key
            dic[k] = dictionary[dic_key]
    
    return dic

def flat_dict(dictionary):
    output = {}
    for key in dictionary:
        
        if isinstance(dictionary[key], dict):
            output.update(flat_concat(key, dictionary[key]))
        else:
            output[key] = dictionary[key]
            
    return output

assert flat_dict({ 'a': 1, 'b': 'foo', 'c': { 'a': 2, 'b': { 'x' : 'zooo', 'z' : 'tooo' } } }) == {'a': 1, 'b': 'foo', 'c_a': 2, 'c_b_x': 'zooo', 'c_b_z': 'tooo'}


'''
Leetcode: https://leetcode.com/problems/fibonacci-number/
hackerrank: ?

Problem: Fibonacci

fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

Example 1:
Input: 4
Output: 3

Example 2:
Input: 10
Output: 55

'''

def fib(n):
	
    if n == 0: return 0
    if n == 1 or n == 2: return 1   
    return fib(n-1) + fib(n-2)


def dynamic_programming_fib(n):
    memo = {}
    if n in memo:
        return memo[n]
    
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    
    res = fib(n-1) + fib(n-2)
    if res not in memo:
        memo[n] = res
        
    return res
	

assert fib(4) == 3
assert fib(10) == 55

'''
leetcode: https://leetcode.com/problems/fizz-buzz/
hackerrank: ?

Problem: Fizz Buzz

Example 1: 
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

'''

def fizzBuzz(n: int):
    output = []
    for i in range(1, n + 1):
        c = ""
        if i % 3 == 0: 
            c = "Fizz"
        if i % 5 == 0: 
            c = c + "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            c = str(i)
        output.append(c)

    return output

fizzbuzz_1 = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
fizzbuzz_2 = ["1","2","Fizz","4","Buzz"]

assert fizzBuzz(15) == fizzbuzz_1
assert fizzBuzz(5) == fizzbuzz_2


'''
leetcode: https://leetcode.com/problems/group-anagrams
hackerrank: ?

Problem: Group Anagrams

Example 1:
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2: 
Input: ["a"]
Output: [["a"]]
'''

def groupAnagrams(strs):
        fm = {}
    
        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word in fm:                                
                fm[sorted_word].append(word)
            else:
                fm[sorted_word] = [word]
                
            
        return [*fm.values()]

assert groupAnagrams(["a"]) == [["a"]]
assert groupAnagrams(["eat","tea","tan","ate","nat","bat"])== [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


'''
leetcode: ?
hackerrank: ?

Problem: Split array into subarrays
Given an array of integers, define a method to split the array into subarrays with the following constraints:
Each subarray only contains unique elements
You use the minimum number of sublists possible
Return the subarrays as an array of arrays.

Example 1:
Input: [1, 2, 3], Output: [[1, 2, 3]]

Example 2:
Input: [1, 2, 2, 3], Output: [[1, 2, 3], [2]]

Example 3:
Input: [1, 2, 2, 2, 3, 3], Output: [[1, 2, 3], [2, 3], [2]]
'''

from collections import Counter
def unique_batches(input):
    fm = Counter(input)
    mf = max(fm.values())
    i = 0
    output = []
    while i < mf:
        output.append([])

        for key in list(fm.keys()):
            fm[key] -= 1
            output[-1].append(key)
            if not fm[key]:
                del fm[key]

        i += 1
    return output

sample_1 = [1, 2, 3]
sample_2 = [1, 2, 2, 3]
sample_3 = [1, 2, 2, 2, 3, 3]
sample_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

assert unique_batches(sample_1) == [[1, 2, 3]]
assert unique_batches(sample_2) == [[1, 2, 3], [2]]
assert unique_batches(sample_3) == [[1, 2, 3], [2, 3], [2]]
assert unique_batches(sample_4) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1]]

'''
leetcode: https://leetcode.com/problems/first-missing-positive/
hackerrank: ?

Problem: First Missing Positive

Example 1:
Input: nums = [3,4,-1,1]
Output: 2

Example 2:
Input: nums = [7,8,9,11,12]
Output: 1

'''

# Time complexity: O(n)
# Space complexity: O(1)

def solution(nums):
        for i in range(len(nums)):                 
            if nums[i] <= 0:
                nums[i] = len(nums) + 1

        for j in range(len(nums)):
            index_to_negative = abs(nums[j]) - 1            
            if index_to_negative >= 0 and index_to_negative < len(nums):
                nums[index_to_negative] = abs(nums[index_to_negative]) * -1    
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
                
        return len(nums) + 1

# Time complexity: O(n)
# Space complexity: O(n)

def solution(arr):
    arr_copy = [None]*len(arr)
    
    for i in range(len(arr_copy)):
        if arr[i] and arr[i] >= 0 and arr[i] <= len(arr):
            arr_copy[i] = 1

    for i in range(len(arr_copy)):
        if arr_copy[i] == None:
            return i+1
    
    return len(arr) + 1
    


# Time complexity: O(n)
# Space complexity: O(n)

def solution(nums):
        nums = set(nums)
        
        for i in range(1,len(nums)+2):
            if i not in nums:
                return i


'''
Problem: Grouping transactions
Input: ['orange', 'apple', 'banana', 'grapes', 'orange']
Output: ['orange 2', 'apple 1', 'banana 1', 'grapes 1']
'''

def group_transactions(transactions):
    output = []
    fm = {}
    for item in transactions:
        fm[item] = fm.get(item, 0) + 1

    for key, value in sorted(list(fm.items()), key=lambda item: (-item[1], item[0])):
        output.append(f'{key} {value}')

    return output

sample = ['orange', 'banana', 'grapes', 'orange', 'grapes', 'grapes', 'grapes', 'grapes', 'grapes', 'melon', 'apple']
response = ['grapes 6', 'orange 2', 'apple 1', 'banana 1', 'melon 1']
assert group_transactions(sample) == response


"""
leetcode: https://leetcode.com/problems/pascals-triangle/
hackerrank: ?

Problem: Pascal's Triangle
"""

def generate(numRows: int):
    output = [[1]]

    for i in range(1, numRows):
        
        arr = [1]
        for j in range(1, i):
            
            r = output[i-1][j] + output[i-1][j-1]
            arr.append(r)
            
        arr.append(1)
        output.append(arr)
        
    return output
    
response = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
assert generate(6) == response


"""
leetcode: ?
hackerrank: ?

Problem: 

Example 1:
Input: 
Output:
"""
