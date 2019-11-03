from typing import List


class Solution:
    @staticmethod
    def longest_common_sequence(x: str, y: str) -> str:
        i, j = len(x), len(y)
        c = [[0 for n in range(j + 1)] for m in range(i + 1)]  # 代表以i,j所在位置结尾的两个字符串的最长公共子序列
        for m in range(i + 1):
            for n in range(j + 1):
                if m == 0 or n == 0:
                    c[m][n] = 0
                else:
                    if x[m - 1] == y[n - 1]:
                        c[m][n] = 1 + c[m - 1][n - 1]
                    else:
                        c[m][n] = max(c[m - 1][n], c[m][n - 1])
        result = ''
        while i > 0 or j > 0:  # 逆推条件顺序要相反，因为x,y的长度不同，会导致c[m][n]==max(c[m][n-1],c[m][n-1])与c[m][n]==c[m-1][n-1]同时成立
            if c[i][j] == c[i - 1][j]:
                i -= 1
            elif c[i][j] == c[i][j - 1]:
                j -= 1
            else:
                result += x[i - 1]
                i -= 1
                j -= 1
        return result[::-1]

    @staticmethod
    def longest_common_string(x: str, y: str) -> str:
        i, j = len(x), len(y)
        c = [[0 for n in range(j + 1)] for m in range(i + 1)]  # 代表以i,j所在位置结尾的两个字符串的最长公共子串
        for m in range(i + 1):
            for n in range(j + 1):
                if m == 0 or n == 0:
                    c[m][n] = 0
                else:
                    if x[m - 1] == y[n - 1]:
                        c[m][n] = 1 + c[m - 1][n - 1]
                    else:
                        c[m][n] = 0

        max_value, max_value_index = -1, -1
        for m in range(i + 1):
            for n in range(j + 1):
                if c[m][n] > max_value:
                    max_value = c[m][n]
                    max_value_index = m
        return x[max_value_index - max_value:max_value_index]

    @staticmethod
    def longest_bigger_sequence(x: List[int]) -> List[int]:
        i = len(x)
        c = [1 for m in range(i)]  # 以i位置的数据结尾的最长递增子序列
        for m in range(1, i):  # 看下数据的比较模式，这个是个n^2的时间复杂度
            for n in range(m, -1, -1):
                if x[m] > x[n]:
                    c[m] = max(c[m], c[n] + 1)

        max_value, max_value_index = -1, -1
        for m in range(i):
            if c[m] > max_value:
                max_value, max_value_index = c[m], m

        result = [x[max_value_index]]
        while max_value_index > -1:
            max_value_index -= 1
            if c[max_value_index] + 1 == max_value:
                result += [x[max_value_index]]
                max_value = c[max_value_index]
        return result[::-1]


if __name__ == '__main__':
    x = 'aabcd'
    y = 'acbc'
    z = [1, 2, 3, 4, 5, 8, 6, 7]
    longest_common_sequence_result = Solution.longest_common_sequence(x, y)
    longest_common_string_result = Solution.longest_common_string(x, y)
    longest_bigger_sequence_result = Solution.longest_bigger_sequence(z)
    print(longest_common_sequence_result)  # abc
    print(longest_common_string_result)  # bc
    print(longest_bigger_sequence_result)
