class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        r = []
        i, j = 0, 0
        count = 0
        loop_count = min(m, n) // 2  # 关键：循环次数（完整能转一圈的次数）取min(m,n)
        while loop_count > 0:
            while j < n - 1 - count:
                r.append(matrix[i][j])
                j += 1
            while i < m - 1 - count:
                r.append(matrix[i][j])
                i += 1
            while j > count:
                r.append(matrix[i][j])
                j -= 1
            while i > count:
                r.append(matrix[i][j])
                i -= 1

            i += 1
            j += 1

            count += 1
            loop_count -= 1
            
        if min(m, n) % 2 != 0:  # 若 min(m,n) 为奇，最后还要处理剩下的最中间的一行/列 特殊情况
            if m < n:
                _i = m // 2
                for _j in range(count, n - count):
                    r.append(matrix[_i][_j])
            else:
                _j = n // 2
                for _i in range(count, m - count):
                    r.append(matrix[_i][_j])

        return r


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3]]))
