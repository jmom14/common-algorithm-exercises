
'''
leetcode: ?
hackerank: ?

Problem: Sliding window

Example:
Input: 
Output: 
'''

def get_diff(a,b):
    if a > b:
        return a - b
    else: 
        return b - a

def segment(x, space):
    maximum = 0
    a = 0
    current = 0
    
    for i in range(0, x - 1):
        maximum = maximum + get_diff(space[i], space[i+1])
    current = maximum
    
    for j in range(1, len(space) - x + 1):
        start_diff = get_diff(space[j], space[j-1])
        end_diff = get_diff(space[j + x - 1], space[j + x - 2])
        
        current = current - start_diff + end_diff
        maximum = max(current, maximum)

    
    return maximum


'''
leetcode: https://leetcode.com/problems/contains-duplicate/
hackerank: ?

Problem: Contains Duplicate

Example:
Input: [1,2,3,1]
Output: true
'''

def containsDuplicate(self, nums) -> bool:
    copy = set()
    
    for num in nums:
        if num in copy:
            return True
        
        copy.add(num)
        
    return False

'''
leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
hackerrank: ?

Problem: Longest Substring Without Repeating Characters

Example: 
Input: "abcabcbb"
Output: 3
'''

def lengthOfLongestSubstring(self, s: str) -> int:
    a = 0
    b = 0
    current = set()
    output = 0
    
    while b < len(s):
        if not s[b] in current:
            current.add(s[b])  
            b+=1
            output = max(output, len(current))
        else:
            current.remove(s[a])
            a+=1
            
    return output

'''
leetcode: https://leetcode.com/problems/reverse-string/description/
hackerrank: ?

Problem: Reverse String

Example:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''

def reverseString(self, s) -> None:
    a = 0
    b = len(s) - 1

    while b > a:
        s[a], s[b] = s[b], s[a]
        a = a + 1
        b = b - 1

    return s


'''
leetcode: https://leetcode.com/problems/reverse-string/description/
hackerrank: ?

Problem: Binary search

Example: 
Input: nums = [1, 5, 9, 10, 14, 16, 78, 100, 121, 122, 123]
Output: true
'''

def binary_search(arr, a, b, search):
    while a <= b:

        mid = a + (b - a) // 2
        if arr[mid] == search:
            return mid
            
        elif arr[mid] > search:
            b = mid - 1
        else: 
            a = mid + 1
    
    return -1
    
nums = [1, 5, 9, 10, 14, 16, 78, 100, 121, 122, 123]
print(binary_search(nums, 0, len(nums) - 1, 123))


'''
leetcode: https://leetcode.com/problems/valid-parentheses/description/
hackerrank: ?

Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


Example 1: 
Input: "([}}])"
Output: False
'''

def isValid(s):
    if not len(s) % 2 == 0:
        return False
    p={ 
        '}': '{',
        ']': '[',
        ')': '(',
    }
    stack = []
    for item in s:
        
        if stack and item in p and stack[-1] == p[item]:
            stack.pop()
        else:
            stack.append(item)

    return len(stack) == 0


assert isValid("([}}])") == False 
assert isValid("()[]{}") == True




'''
leetcode: ?
hackerrank: ?

Problem: 

Example: 
Input: 
Output: 
'''

