class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in pairs.keys():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return 0
                a = stack.pop()
                if i!=pairs[a]:
                    return 0
        return len(stack)==0
