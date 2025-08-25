class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        translate_s_t = {}
        translate_t_s = {}
        for c_s, c_t in zip(s, t):
            if (c_s not in translate_s_t) and (c_t not in translate_t_s):
                translate_s_t[c_s] = c_t
                translate_t_s[c_t] = c_s
            elif (translate_s_t.get(c_s) != c_t) or (translate_t_s.get(c_t) != c_s):
                return False
        
        return True