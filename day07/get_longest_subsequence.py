"""
2900. 最长相邻不相等子序列 I
    给你一个下标从 0 开始的字符串数组 words ，和一个下标从 0 开始的 二进制 数组 groups ，两个数组长度都是 n 。
    你需要从 words 中选出 最长子序列。
    如果对于序列中的任何两个连续串，二进制数组 groups 中它们的对应元素不同，则 words 的子序列是不同的。
    正式来说，你需要从下标 [0, 1, ..., n - 1] 中选出一个 最长子序列 ，将这个子序列记作长度为 k 的 [i0, i1, ..., ik - 1] ，
    对于所有满足 0 <= j < k - 1 的 j 都有 groups[ij] != groups[ij + 1] 。
    请你返回一个字符串数组，它是下标子序列 依次 对应 words 数组中的字符串连接形成的字符串数组。
    如果有多个答案，返回 任意 一个。
    注意：words 中的元素是不同的 。
    示例 1：
            输入：words = ["e","a","b"], groups = [0,0,1]
            输出：["e","b"]
            解释：一个可行的子序列是 [0,2] ，因为 groups[0] != groups[2] 。
            所以一个可行的答案是 [words[0],words[2]] = ["e","b"] 。
            另一个可行的子序列是 [1,2] ，因为 groups[1] != groups[2] 。
            得到答案为 [words[1],words[2]] = ["a","b"] 。
            这也是一个可行的答案。
            符合题意的最长子序列的长度为 2 。
    示例 2：
            输入：words = ["a","b","c","d"], groups = [1,0,1,1]
            输出：["a","b","c"]
            解释：一个可行的子序列为 [0,1,2] 因为 groups[0] != groups[1] 且 groups[1] != groups[2] 。
            所以一个可行的答案是 [words[0],words[1],words[2]] = ["a","b","c"] 。
            另一个可行的子序列为 [0,1,3] 因为 groups[0] != groups[1] 且 groups[1] != groups[3] 。
            得到答案为 [words[0],words[1],words[3]] = ["a","b","d"] 。
            这也是一个可行的答案。
            符合题意的最长子序列的长度为 3 。
"""
from itertools import pairwise
from typing import List


# 方法一：
def getLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
    best_indices = []  # 用于记录最佳子序列的下标列表
    n = len(groups)
    # 枚举每个可能的起始点
    for start in range(n):
        current_indices = [start]
        last_group = groups[start]
        # 从起始点往后遍历，收集相邻不同组的下标
        for i in range(start + 1, n):
            if groups[i] != last_group:
                current_indices.append(i)
                last_group = groups[i]
        if len(current_indices) > len(best_indices):
            best_indices = current_indices
    return [words[i] for i in best_indices]


# 方法二：
def get_longest_subsequence(words, groups):
    result = [words[0]]
    last_group = groups[0]

    for i in range(1, len(words)):
        if groups[i] != last_group:
            result.append(words[i])
            last_group = groups[i]

    return result


# 方法三：
def get_longest_subsequence1(words, groups):
    n = len(words)
    return [words[i] for i in range(n)
            if i == n - 1
            or groups[i] != groups[i + 1]]


# 方法四：
def get_longest_subsequence2(words, groups):
    return ([w for (x, y), w in zip(pairwise(groups), words)
             if x != y]
            + [words[-1]])


words = ["a", "b", "c", "d"]
groups = [1, 0, 1, 1]
print(getLongestSubsequence(words, groups))
