class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        txt = s[::-1]
        # start = False
        length = 0

        for character in txt:
            if character == " " and length == 0:
                start = False
            elif character != " ":
                # start = True
                length += 1
            else:
                return length

        return length
            