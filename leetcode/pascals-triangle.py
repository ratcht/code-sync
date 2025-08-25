class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(0, numRows):
            sub = []
            for j in range(0, i + 1):
                if j == 0: sub.append(1)
                elif j == i: sub.append(1)
                else:
                    above = res[i-1]
                    num = above[j] + above[j-1]
                    sub.append(num)

            res.append(sub)
        return res