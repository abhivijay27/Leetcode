class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS,countT = {},{}
        if(len(s)!=len(t)):
            return 0
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)
        for c in countS:
            if countS[c]!=countT.get(c,0):
                return 0
        return 1
      
     The below doesnt work for large i/ps 
#   def isAnagram(s: str, t: str):
#     i,j = 0,0
#     visit = set()
#     m,n = len(s), len(t)
#     if(m!=n):
#         return 0
#     while i<m and j<n:
#         if s[i] == t[j] and j not in visit:
#             #print("In if")
#             visit.add(j)
#             i+=1
#             j=0
#         else:
#             #print("In else")
#             j+=1
#         if i<m and j==n:
#             #print("In j=n if")
#             i+=1
#             j=0
#     if len(visit) == m:
#         return 1
#     else: 
#         #print(visit)
#         return 0
# if __name__ == "__main__":
#     s = 'car'
#     t = 'rat'
#     f = isAnagram(s,t)
#     if f==0:
#         print("false")
#     else:
#         print("true")
                   
