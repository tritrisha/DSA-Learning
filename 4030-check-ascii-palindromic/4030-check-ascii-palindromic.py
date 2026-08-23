class Solution:
    def isPalindromic(self, s: str) -> bool:
        ascii = [f"{ord(char):08b}" for char in s]
        ascii="".join(ascii)

        return ascii==ascii[::-1]