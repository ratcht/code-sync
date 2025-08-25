class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        unique = 1


        while i < len(nums):
            if nums[i] == nums[unique] == nums[unique - 1]:
                # nums[unique] = nums[i]
                i += 1
                # unique += 1
            else:
                nums[unique + 1] = nums[i]
                i += 1
                unique += 1
                

        return unique + 1