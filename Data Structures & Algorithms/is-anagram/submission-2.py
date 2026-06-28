class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #    s_d=defaultdict(str=0)
       s_d={}
       t_d={}
    #    t_d=defaultdict(str = 0)
       for i in s:
            if i in s_d.keys():
                s_d[i]+=1
            else:
                s_d[i]=1

       for i in t:
            if i in t_d.keys():

                t_d[i]+=1
            else:
                t_d[i]=1
       for k,v in s_d.items():
            if k not in t_d.keys():
                return False
            if t_d[k]!=v:
                return False
       for k,v in t_d.items():
            if k not in s_d.keys():
                return False
            if s_d[k]!=v:
                return False
       return True

