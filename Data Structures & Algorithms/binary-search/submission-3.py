class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        k = round((i + j) / 2)
        while (i + 1 < j):
            if(target == nums[k]):
                return k
            elif(target < nums[k]):
                j = k
            else:
                i = k
            k = round((i + j) / 2)
        if(nums[k] == target):
            return k
        if(nums[i] == target):
            return i
        if(nums[j] == target):
            return j
        return -1