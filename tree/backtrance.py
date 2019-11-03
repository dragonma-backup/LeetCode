from typing import List


class Solution:

    @staticmethod
    def combination_sum_repeat(candidates: List[int], target: int) -> List[List[int]]:
        def __dfs(candidates, start, target, path, result):
            if target == 0:
                result.append(path[:])
            for i in range(start, len(candidates)):
                residue = target - candidates[i]
                if residue < 0:
                    break
                path.append(candidates[i])
                __dfs(candidates, i, residue, path, result)
                path.pop()

        candidates.sort()
        path = []
        result = []
        __dfs(candidates, 0, target, path, result)
        return result

    @staticmethod
    def combination_sum_single(candidates: List[int], target: int) -> List[List[int]]:
        def __dfs(candidates, start, target, path, result):
            if target == 0:
                result.append(path[:])
            for i in range(start, len(candidates)):
                residue = target - candidates[i]
                if residue < 0:
                    break
                path.append(candidates[i])
                __dfs(candidates, i + 1, residue, path, result)
                path.pop()

        candidates.sort()
        path = []
        result = []
        __dfs(candidates, 0, target, path, result)
        return result

    @staticmethod
    def combination_sum_repeat_layer(candidates: List[int], target: int, layer: int) -> List[List[int]]:
        def __dfs(candidates, start, target, layer, path, result):
            if target == 0 and layer == 0:
                result.append(path[:])
            for i in range(start, len(candidates)):
                residue = target - candidates[i]
                sub_layer = layer - 1
                if residue < 0 or sub_layer < 0: # 改下条件函数就行了
                    break
                path.append(candidates[i])
                __dfs(candidates, i, residue, sub_layer, path, result)
                path.pop()

        candidates.sort()
        path = []
        result = []
        __dfs(candidates, 0, target, layer, path, result)
        return result


if __name__ == '__main__':
    candidates = [i for i in range(1, 10)]
    path, result = [], []
    target = 5
    layer = 3
    combination_sum_repeat_result = Solution.combination_sum_repeat(candidates, target)
    combination_sum_single_result = Solution.combination_sum_single(candidates, target)
    combination_sum_repeat_layer_result = Solution.combination_sum_repeat_layer(candidates, target, layer)
    print(combination_sum_repeat_result)
    print(combination_sum_single_result)
    print(combination_sum_repeat_layer_result)
