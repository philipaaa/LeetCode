class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to their integer values
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        count = 0
        n = len(s)
        
        for i in range(n):
            # Check if the current numeral is smaller than the next
            if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                count -= roman_to_int[s[i]]  # Subtract current value
            else:
                count += roman_to_int[s[i]]  # Add current value
        
        return count