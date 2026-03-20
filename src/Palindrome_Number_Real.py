class Solution(object):
    def isPalindrome(self, x):
        #x= 1000021  
        s= str(x) # add mod for true palindrome
        left= 0
        right= 0
        d= 5

        for i in range(len(s)):
        # for i in range(x): race from 0tox
            print(s[i])

            left = i
            right = len(s)-1-i 
            charleft = s[left]  # fetching charac value at the index string
            charright = s[right]  # fetching charac value at the iaandex string
            if (charleft != charright):

                
                    print("not palindrome")
                    return False
                    break     
        return True

# Below didnt work on Test case 1000021 as continued to run Code part 2 : 
class Solution(object):
    def isPalindrome(self, x):
            
        s= str(x)  # add mod for true palindrome
        left= 0
        right= 0

        for i in range(len(s)):
        # for i in range(x): race from 0tox
            print(s[i])

            left = i
            right = len(s)-1-i 
            charleft = s[left]  # fetching charac value at the index string
            charright = s[right]  # fetching charac value at the index string
            if (charleft == charright):
                    print (charleft,"matched",charright)
                    return True
            else:
                    print("not palindrome")
                    return False


  
    
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:  -231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
