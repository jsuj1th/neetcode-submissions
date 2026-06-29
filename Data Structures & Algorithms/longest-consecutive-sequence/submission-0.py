class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(sorted(nums))
        print(nums)
        l=0
        i=0
        start_points=[]
        for i in nums:
            if i-1 not in nums:
                start_points.append(i)
        # print(start_points)
        for i in start_points:
            j=i
            count=1
            while j+1 in nums:
                j+=1
                count+=1
            
            l=max(count,l)
        return l
        # while i <len(nums):
        #     if nums[i]-1!=nums[i-1]:
        #         c=0
        #         while nums[i]+1==nums[i+1]:
        #             c+=1
        #             i+=1
        #         if c> l:
        #             l=c
        #     i+=1   
        # return l

