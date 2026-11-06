class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val:index

        for i, n in enumerate(nums):
            diff = target - n #looks for if target and its difference is in the hashmap
            if diff in prevMap: #if our target is located return 
                return [prevMap[diff], i]
            prevMap[n] = i
        return
        