from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def __dfs(candidates: List[int], index: int, n: int, k: int, path: List[int], result: List[List[int]]):
            if k == 0 and n == 0:  # 限制个数，如果是至多的情况，就直接去掉n就行了
                result.append(path[:])
            for i in range(index, len(candidates)):
                residue = k - candidates[i]
                sub_n = n - 1
                if k < 0 or sub_n < 0:
                    break
                path.append(candidates[i])
                __dfs(candidates, i, sub_n, residue, path, result)
                path.pop()

        candidates = [i for i in range(1, 10)]
        path = []
        result = []
        __dfs(candidates, 0, n, k, path, result)
        return result


class Tree:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    @staticmethod
    def bfs(tree):  # 使用队列的进出实现
        result = []
        queue = []
        if tree:
            queue.append(tree)
        while len(queue) > 0:
            head = queue.pop(0)
            result.append(head.value)
            if head.left_node:
                queue.append(head.left_node)
            if head.right_node:
                queue.append(head.right_node)
        return result

    @staticmethod
    def dfs(tree):
        def __post_result(pre_result, mid_result):
            if len(pre_result) == 1:
                return pre_result[:]
            else:
                root = pre_result[0]
                mid_root_index = mid_result.index(root)
                return __post_result(pre_result[1:1 + mid_root_index], mid_result[:mid_root_index]) + \
                       __post_result(pre_result[-mid_root_index:], mid_result[-mid_root_index:]) + \
                       [root]

        pre_result = []
        mid_result = []
        stack = []

        while tree or len(stack) > 0:
            if tree:  # 搜索中只出现一个指针 while(tree)+ if(len(stack>0)) 是一致的，该子代码区域内只有3中可能性
                stack.append(tree)  # 入栈
                pre_result.append(tree.value)
                tree = tree.left_node
            else:
                tree = stack.pop()  # 出栈
                mid_result.append(tree.value)
                tree = tree.right_node
        return pre_result, mid_result, __post_result(pre_result, mid_result)

    @staticmethod
    def post_dfs(tree):  # 左右中 中左右，左中右，所以左右中相当于左右互换，然后先序遍历
        result = []
        stack = []
        while tree or len(stack) > 0:
            if tree:
                stack.append(tree)
                result.append(tree.value)
                tree = tree.right_node
            else:
                tree = stack.pop()
                tree = tree.left_node
        return result[::-1]


if __name__ == '__main__':
    # solution = Solution()
    # k = 4
    # n = 2
    # combinationSum3_reslut = solution.combinationSum3(k, n)
    # print(combinationSum3_reslut)

    tree1 = Tree(2, Tree(4, None, None), Tree(5, None, None))
    tree2 = Tree(3, Tree(6, None, None), Tree(7, None, None))
    root = Tree(1, tree1, tree2)
    bfs_result = Tree.bfs(root)
    pre_result, mid_result, post_result = Tree.dfs(root)
    post_result1 = Tree.post_dfs(root)
    print(bfs_result, pre_result, mid_result, post_result)
    print(post_result1)
