class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        flat = [num for row in grid for num in row]
        flat.sort()
        cou=0
        l=len(flat)
        y=flat[l//2]
        rem=y%x
        for i in range(l):
            if flat[i]%x!=rem:
                return -1

            cou+=abs(flat[i]-y)

        return cou//x



        