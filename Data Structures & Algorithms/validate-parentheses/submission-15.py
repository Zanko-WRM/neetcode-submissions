class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        s_v =[]
        for i in range(len(s)):
            if s[i] in "{[(":
                s_v.append(s[i])
            elif s[i] in "}])":
                if not s_v:
                    return False

                if s[i] == "}":
                    if s_v[-1] == '{':
                        s_v.pop()
                    else:
                        return False
                elif s[i] == "]":
                    if s_v[-1] == '[':
                        s_v.pop()
                    else:
                        return False
                elif s[i] == ")":
                    if s_v[-1] == '(':
                        s_v.pop()
                    else:
                        return False
        
        return len(s_v) == 0

