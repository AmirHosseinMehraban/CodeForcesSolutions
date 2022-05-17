from pickle import TRUE
from re import S


class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if s[0]=="}" or s[0]==")" or s[0]=="]":
            return False
        if len(s)%2!=0:
            return False
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif stack==[]:
                return False
            elif i==')':
                if stack[-1]!='(':
                    return False
                stack.pop()
            elif i==']':
                if stack[-1] !='[':
                    return False
                stack.pop()
            elif i=='}':
                if stack[-1]!='{':
                    return False
                stack.pop()
        if stack==[]:
            return True
        else:
            return False

p=Solution()
print(p.isValid("()[]"))
