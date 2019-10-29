class Solution:
    def longest_common_sequence(self, x: str, y: str) -> str:
        i, j = len(x), len(y)
        c = [[0 for n in range(j + 1)] for m in range(i + 1)]
        for m in range(i + 1):
            for n in range(j + 1):
                if m == 0 or n == 0:
                    c[m][n] = 0
                else:
                    if x[m - 1] == y[n - 1]:
                        c[m][n] = c[m - 1][n - 1] + 1
                    else:
                        c[m][n] = max(c[m - 1][n], c[m][n - 1])  # 不连续max,两个直接比较矩阵，一个与自身进行比较（最长子序列和最长递增子序列）

        common_sequence = ''
        while i > 0 or j > 0:
            if c[i][j] == c[i - 1][j - 1] + 1:
                common_sequence += x[i - 1]
                i = i - 1
                j = j - 1
            else:
                if c[i][j] == c[i - 1][j]:
                    i = i - 1
                else:
                    j = j - 1
        return common_sequence[::-1]

    def longest_common_string(self, x: str, y: str) -> str:
        i, j = len(x), len(y)
        c = [[0 for n in range(j + 1)] for m in range(i + 1)]
        for m in range(i + 1):
            for n in range(j + 1):
                if m == 0 or n == 0:
                    c[m][n] = 0
                else:
                    if x[m - 1] == y[n - 1]:
                        c[m][n] = c[m - 1][n - 1] + 1
                    else:
                        c[m][n] = 0

        maxm, maxvalue = -1, -1
        for m in range(i + 1):
            for n in range(j + 1):
                if c[m][n] > maxvalue:
                    maxm, maxvalue = m, c[m][n]

        return x[maxm - maxvalue:maxm]

    def longest_bigger_sequence(self, x: list) -> list:
        i = len(x)
        c = [1 for i in range(i)]
        for m in range(i):
            for n in range(m, -1, -1):
                if x[n] < x[m]:
                    c[m] = max(c[m], c[n] + 1)

        maxi = c.index(max(c))
        bigger_sequence = [c[maxi]]
        flag = c[maxi]
        m = maxi - 1
        while m > -1:
            if flag == c[m] + 1:
                bigger_sequence += [c[m]]
                flag = c[m]
            m -= 1
        return bigger_sequence[::-1]


if __name__ == '__main__':
    solution = Solution()
    x = 'abcac'
    y = 'abccacc'
    longest_common_sequence_result = solution.longest_common_sequence(x, y)
    longest_common_string_result = solution.longest_common_string(x, y)
    longest_bigger_sequence_result = solution.longest_bigger_sequence([1, 2, 3, 1, 1, 4, 5])
    print(longest_common_sequence_result)
    print(longest_common_string_result)
    print(longest_bigger_sequence_result)
