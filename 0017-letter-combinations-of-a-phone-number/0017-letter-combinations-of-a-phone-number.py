class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def combo(x, p):
            if x>=len(digits):
                k.append(p)
                return

            for i in phone_map[digits[x]]:
                p+=i
                combo(x+1, p)
                p=p[:-1]

        k=[]
        combo(0, '')
        return k

        