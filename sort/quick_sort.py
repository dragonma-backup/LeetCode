from typing import List


class Solution:
    '''
    quick_sort:(双指针（进一步减半，nlog(n/2)）是绝对不能保证稳定性的，如果是单指针并保证后置同值数据大于flag则能保证稳定性)
        1. 确定flag
        2. 双指针交换（比较方便）
        3. 二分quick_sort
    '''

    @staticmethod
    def quick_sort(x: List[int]) -> List[int]:  # quik_sort不能保证稳定性 nlog(n)
        if len(x) == 0 or len(x) == 1:  # 递归结束条件
            return x
        f = x[0]
        i = 1
        j = len(x) - 1
        while i < j:  # 双指针，不需要额外空间开销(单指针，并且规定后置的相等数据大于该值，则可以''保证稳定性'')
            if x[i] < f <= x[j]:
                i += 1
                j -= 1
                continue
            if x[i] >= f > x[j]:
                x[i], x[j] = x[j], x[i]
                i += 1
                j -= 1
                continue
            if x[i] < f and x[j] < f:
                x.insert(i + 1, x.pop(j))
                i += 2
                continue
            if x[i] >= f and x[j] >= f:
                x.insert(j - 1, x.pop(i))
                j -= 2
        f_index = 0
        if i == j and x[i] < f:
            f_index = i
            x[0], x[f_index] = x[i], f
        else:
            f_index = i - 1
            x.insert(f_index, x.pop(0))
        x[:f_index] = Solution.quick_sort(x[:f_index])
        x[f_index + 1:] = Solution.quick_sort(x[f_index + 1:])
        return x


if __name__ == '__main__':
    x = [5, 2, 7, 3, 8, 1, 3, 5]
    quick_sort_result = Solution.quick_sort(x)
    print(quick_sort_result)
