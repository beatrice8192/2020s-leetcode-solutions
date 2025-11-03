# https://leetcode.com/problems/image-smoother
class Solution(object):
    # def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(img)
        columns = len(img[0])
        output_ = [[0 for c in range(columns)] for r in range(rows)]
        for r in range(rows):
            for c in range(1, columns - 1):
                output_[r][c] = sum(img[r][c-1:c+2])
            output_[r][0] = sum(img[r][:2])
            output_[r][-1] = sum(img[r][-2:])
        output = [[output_[r][c] for c in range(columns)] for r in range(rows)]
        for c in range(columns):
            for r in range(1, rows - 1):
                output[r][c] = sum((x[c] for x in output_[r-1:r+2]))
            output[0][c] = sum((x[c] for x in output_[:2]))
            output[-1][c] = sum((x[c] for x in output_[-2:]))
        for r in range(rows):
            r_divisor = 1
            if (r > 0):
                r_divisor += 1
            if (r < rows - 1):
                r_divisor += 1
            for c in range(columns):
                c_divisor = 1
                if (c > 0):
                    c_divisor += 1
                if (c < columns - 1):
                    c_divisor += 1
                output[r][c] = int(output[r][c] / r_divisor / c_divisor)
        return output

