class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if(m.get(target - nums[i], -1) != -1):
                return [ m.get(target - nums[i]), i ]
            if(m.get(nums[i], -1) == -1):
                m[nums[i]] = i