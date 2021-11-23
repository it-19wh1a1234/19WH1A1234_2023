class Solution:
    def isValid(self, s: str) -> bool:
        a1 = []
        for i in s:
            if i in ['{','[','(']:
                a1.append(i)
            else:
                if not a1:
                    return False
                if a1[-1]=='{' and i=='}' or a1[-1]=='[' and i==']' or a1[-1]=='(' and i==')':
                    a1.pop()
                    continue
                else:
                    return False
        if a1:
            return False
        return True
