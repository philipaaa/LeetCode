class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Pointers for s and t
        s_ptr, t_ptr = 0, 0

        # Traverse both strings
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1  # Move the s pointer if characters match
            t_ptr += 1  # Always move the t pointer
        
        # If s_ptr has reached the end of s, all characters in s were found in order
        return s_ptr == len(s)