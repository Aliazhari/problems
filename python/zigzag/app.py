# ******************************************
#  Author : Ali Azhari 
#  Created On : Tue Jul 23 2019
#  File : app.py
# *******************************************/


class Solution:

    def convert(self, s, numRows):

        if numRows == 1: return s

        rows = []
        for _ in range(0, numRows):
            rows.append('')

       
        curRow = 0
        goingDown = False

        for c in s:
            rows[curRow] += c
            print(curRow, rows[curRow])
            if (curRow == 0 or curRow == numRows - 1): goingDown = not goingDown
            curRow += 1 if goingDown else -1
           
        ret = ''
        for row in rows: ret += row
        return ret

solution = Solution()
print(solution.convert('PAYPALISHIRING', 3))

# P   A   H   N
# A P L S I I G
# Y   I   R
