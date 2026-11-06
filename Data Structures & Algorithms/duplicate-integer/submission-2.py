'''
1. Understand
-sort through a list of numbers
-based on the list of numbers if the list has repeated numbers return 'true' else 'false'
-if list is empty return 'false'

2. Plan
    (1) create a new list of numbers using set()
    (2) compare each the nums list to the new list
    (3) if they match return 'false' and 'true' other wise
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n = set(nums)

        if len(n) != len(nums):
            return True
        else:
            return False


        
