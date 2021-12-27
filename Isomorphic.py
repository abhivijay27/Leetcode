class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS,mapT = {},{}
        for i,j in zip(s,t):
            if (i in mapS and mapS[i]!=j) or (j in mapT and mapT[j]!=i):
                return 0
            mapS[i] = j
            mapT[j] = i
        return 1
        
