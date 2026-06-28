class Solution:

    def encode(self, strs: List[str]) -> str:
        k=""
        for s in strs:
            l=len(s)
            k+=(str(l)+"#"+s)
        print(k)
        return k
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            j=i
            while s[j] !="#":
                j+=1
            l=int(s[i:j])
            k=s[j+1:j+1+l]
            res.append(k)
            i=j+1+l
        return res