class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # always jump to highest possible number
        jump = 0
        for n in nums:
            if jump < 0: return False
            
            if n > jump:
                jump = n
            jump -= 1
        
        return True