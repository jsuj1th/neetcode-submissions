class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        # print(nums)
        l=0
        i=0
        start_points=[]
        for i in nums:
            if i-1 not in nums:
                start_points.append(i)

        for i in start_points:
            j=i
            count=1
            while j+1 in nums:
                j+=1
                count+=1
            l=max(count,l)
        return l
        

