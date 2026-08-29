class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r=0
        for i in columnTitle:
            r=26*r+ (ord(i)-64)
        return r

        