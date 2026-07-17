class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        start = 0
        n = len(nums)
        
        for i in range(n-1):
            if nums[i+1] - nums[i] > 1:
                if start == i:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i]}")
                start =i + 1
                
        if start == n - 1:
            result.append(str(nums[start]))
        else:
            result.append(f"{nums[start]}->{nums[n - 1]}")
        return result 