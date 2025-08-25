class Solution:
    
    
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        max_reachable = 0
        last_jumped_pos = 0
        jumps = 0

        while last_jumped_pos < n-1:
            max_reachable = max(max_reachable, i + nums[i])
            if i == last_jumped_pos:
                last_jumped_pos = max_reachable
                jumps += 1
                
            i += 1
        return jumps