class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                # Shorten the prefix until it matches
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix