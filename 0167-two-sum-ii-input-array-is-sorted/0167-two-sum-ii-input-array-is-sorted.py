class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # convert to 1-indexed
            elif current_sum < target:
                left += 1   # sum too small, need a bigger number -> move left pointer right
            else:
                right -= 1  # sum too big, need a smaller number -> move right pointer left
        
        return []  # problem guarantees a solution, so this won't trigger