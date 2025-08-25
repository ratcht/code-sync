class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        current_sum = 0
        min_length = float('inf')
        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]

            if current_sum < target:
                continue
            
            # current sum >= target:
            while current_sum >= target:
                # print(f"r: {right}. l: {left}")
                if current_sum >= target:
                    min_length = min(min_length, right - left + 1)
                else:
                    break
                current_sum -= nums[left]
                left += 1
        
        if min_length == float('inf'): return 0
        return min_length