class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        h={}
        for i in words:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1

        r=list(dict(sorted(h.items(), key= lambda item:item[1], reverse=True)))

        return r[:k]
        