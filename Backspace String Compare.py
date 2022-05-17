class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s=[]
        stack_t=[]
        for i in s:
            if i=="#":
                if len(stack_s)==0:
                    pass
                else:
                    stack_s.pop()
            else:
                stack_s.append(i)
        for i in t:
            if i=="#":
                if len(stack_t)==0:
                    pass
                else:
                    stack_t.pop()
            else:
                stack_t.append(i)
        if stack_t==stack_s:
            return True
        return False
p=Solution()
print(p.backspaceCompare("ab#c","ad#c"))