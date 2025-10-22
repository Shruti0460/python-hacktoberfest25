# Find Most Frequent Vowel and Consonant

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = set("aeiou")
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        vowel = 0
        consonant = 0
        for ch, count in freq.items():
            if ch in vowels:
                vowel = max(vowel, count)

            else:
                consonant = max(consonant, count)

        return vowel + consonant 
