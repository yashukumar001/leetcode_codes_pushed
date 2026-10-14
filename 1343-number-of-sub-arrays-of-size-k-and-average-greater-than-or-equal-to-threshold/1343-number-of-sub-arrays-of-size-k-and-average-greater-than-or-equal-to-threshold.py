class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window_sum =sum(arr[:k])
        count = 0
        req_sum = k * threshold 

        if window_sum >= req_sum:
            count+=1
        for right in range(k,len(arr)):
            window_sum -= arr[right-k]
            window_sum += arr[right]
            if window_sum >= req_sum:
                count+=1
        return count
            