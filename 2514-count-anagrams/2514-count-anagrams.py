class Solution:
    def countAnagrams(self, s: str) -> int:
        mod = 1000000007
        words = s.split(' ')
        max_len = len(max(words, key=len))
        fact = [1] * (max_len + 1)
        for i in range(2, max_len + 1):
            fact[i] = fact[i - 1] * i % mod
        inv_fact = [1] * (max_len + 1)
        inv_fact[max_len] = pow(fact[max_len], mod - 2, mod)
        for i in range(max_len, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % mod

        ans = 1
        for word in words:
            count = {}
            for ch in word:
                count[ch] = count.get(ch, 0) + 1
            ans = ans * fact[len(word)] % mod
            for freq in count.values():
                ans = ans * inv_fact[freq] % mod

        return ans
           
           



        