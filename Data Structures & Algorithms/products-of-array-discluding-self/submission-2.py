class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        fp=[0]*n
        bp=[0]*n
        f=1
        b=1
        for i in range(n):
            f*=nums[i]
            b*=nums[n-1-i]
            fp[i]=f
            bp[n-1-i]=b
        ans=[0]*n
        ans[0]=bp[1]
        ans[-1]=fp[-2]
        # print(fp)
        # print(bp)
        # print(ans)
        for i in range(1,n-1):
            ans[i]=fp[i-1]*bp[i+1]
            # print(ans)
        return ans
            