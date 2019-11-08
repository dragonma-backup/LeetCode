from typing import List


class Solution:
    '''
    1. 构建堆
    2. 堆排序
    3. 调整堆
    '''

    @staticmethod
    def heap_sort(x: List[int]) -> List[int]:
        def build(x):  # 第一次要建出最大堆
            for i in range(len(x) // 2 - 1, -1, -1):
                adjust(x, i)

        def adjust(x, i):
            left_index = i * 2 + 1
            right_index = i * 2 + 2
            left_exchange = False
            right_exchange = False
            if left_index < len(x) and x[left_index] > x[i]:
                x[left_index], x[i] = x[i], x[left_index]
                left_exchange = True
            if right_index < len(x) and x[right_index] > x[i]:
                x[right_index], x[i] = x[i], x[right_index]
                right_exchange = True
            if left_exchange:
                adjust(x, left_index)
            if right_exchange:
                adjust(x, right_index)
            return x

        # way1
        build(x)  # 这种方式不需要额外的空间，直接利用原始数组
        for i in range(len(x)):
            x[0], x[-(i + 1)] = x[-(i + 1)], x[0]  # heap_sort
            x[:-(i + 1)] = adjust(x[:-(i + 1)], 0)
        return x

        # way2
        # build(x)
        # result = []
        # for i in range(len(x)):
        #     result.append(x.pop(0)) # heap_sort
        #     adjust(x, 0)
        # return result[::-1]

    @staticmethod
    def find_k_th_largest(x: List[int], k: int) -> List[int]:
        def build(x):
            for i in range((len(x) - 2) // 2, -1, -1):
                adjust(x, i)

        def adjust(x, i):
            left_index = i * 2 + 1
            right_index = i * 2 + 2
            left_exchange = False
            right_exchange = False
            if left_index < len(x) and x[left_index] > x[i]:
                x[left_index], x[i] = x[i], x[left_index]
                left_exchange = True
            if right_index < len(x) and x[right_index] > x[i]:
                x[right_index], x[i] = x[i], x[right_index]
                right_exchange = True
            if left_exchange:
                adjust(x, left_index)
            if right_exchange:
                adjust(x, right_index)

        result = []
        build(x)
        while len(result) < k:
            x[0], x[-1] = x[-1], x[0]  # heap_sort
            result.append(x.pop())  # 直接置换会影响原始堆中的结构
            adjust(x, 0)
        return result[-1]


if __name__ == '__main__':
    x = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    # heap_sort_result = Solution.heap_sort(x)
    k_th_largest_result = Solution.find_k_th_largest(x, k)
    # print(heap_sort_result)
    print(k_th_largest_result)
