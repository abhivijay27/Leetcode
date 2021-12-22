class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            s = 0
            while n>0:
                d = n%10
                d = d*d
                s = s+d
                n = n//10
            n = s
            if n == 1:
                return 1
        return 0 
