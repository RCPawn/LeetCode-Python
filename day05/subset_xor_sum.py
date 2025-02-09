"""
1863. 找出所有子集的异或总和再求和
    一个数组的 异或总和 定义为数组中所有元素按位 XOR 的结果；如果数组为 空 ，则异或总和为 0 。
    例如，数组 [2,5,6] 的 异或总和 为 2 XOR 5 XOR 6 = 1 。
    给你一个数组 nums ，请你求出 nums 中每个 子集 的 异或总和 ，计算并返回这些值相加之 和 。
    注意：在本题中，元素 相同 的不同子集应 多次 计数。
    数组 a 是数组 b 的一个 子集 的前提条件是：从 b 删除几个（也可能不删除）元素能够得到 a 。
    示例 1：
            输入：nums = [1,3]
            输出：6
            解释：[1,3] 共有 4 个子集：
                - 空子集的异或总和是 0 。
                - [1] 的异或总和为 1 。
                - [3] 的异或总和为 3 。
                - [1,3] 的异或总和为 1 XOR 3 = 2 。
                0 + 1 + 3 + 2 = 6
    示例 2：
            输入：nums = [5,1,6]
            输出：28
            解释：[5,1,6] 共有 8 个子集：
                - 空子集的异或总和是 0 。
                - [5] 的异或总和为 5 。
                - [1] 的异或总和为 1 。
                - [6] 的异或总和为 6 。
                - [5,1] 的异或总和为 5 XOR 1 = 4 。
                - [5,6] 的异或总和为 5 XOR 6 = 3 。
                - [1,6] 的异或总和为 1 XOR 6 = 7 。
                - [5,1,6] 的异或总和为 5 XOR 1 XOR 6 = 2 。
                0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
    示例 3：
            输入：nums = [3,4,5,6,7,8]
            输出：480
            解释：每个子集的全部异或总和值之和为 480 。
"""
from typing import List


# 方法一：位运算 + 枚举
def subsetXORSum(nums: List[int]) -> int:
    total, n = 0, len(nums)

    for mask in range(1 << n):  # 共有 1 x 2 ^ n 个子集
        xor_sum = 0  # 当前子集的异或和
        for i in range(n):
            if mask & (1 << i):  # 判断当前元素是否在子集中
                xor_sum ^= nums[i]  # 计算子集的异或和
        total += xor_sum  # 累加所有子集的异或和

    return total  # 返回最终的异或总和


"""
dfs(0, 0)  # 处理第 0 个数：1
├── dfs(1, 1)  # 选择 1（val ^ 1 = 1）
│   ├── dfs(3, 2)  # 选择 2（1 ^ 2 = 3）
│   │   ├── dfs(0, 3)  # 选择 3（3 ^ 3 = 0）✅ 终止
│   │   ├── dfs(3, 3)  # 不选择 3（3 继续）✅ 终止
│   ├── dfs(1, 2)  # 不选择 2（1 继续）
│       ├── dfs(2, 3)  # 选择 3（1 ^ 3 = 2）✅ 终止
│       ├── dfs(1, 3)  # 不选择 3（1 继续）✅ 终止
├── dfs(0, 1)  # 不选择 1（0 继续）
    ├── dfs(2, 2)  # 选择 2（0 ^ 2 = 2）
    │   ├── dfs(1, 3)  # 选择 3（2 ^ 3 = 1）✅ 终止
    │   ├── dfs(2, 3)  # 不选择 3（2 继续）✅ 终止
    ├── dfs(0, 2)  # 不选择 2（0 继续）
        ├── dfs(3, 3)  # 选择 3（0 ^ 3 = 3）✅ 终止
        ├── dfs(0, 3)  # 不选择 3（0 继续）✅ 终止
"""


# 方法二：回溯（DFS）
def subsetXORSum1(nums):
    def dfs(val, i):
        nonlocal total
        if i == n:  # 遍历完所有元素
            total += val  # 记录当前子集的异或和
            return

        # 选择当前元素，异或计算后进入下一层递归
        dfs(val ^ nums[i], i + 1)
        # 不选择当前元素，直接进入下一层递归
        dfs(val, i + 1)

    total, n = 0, len(nums)
    dfs(0, 0)
    return total


nums = [3, 4, 5, 6, 7, 8]
print(subsetXORSum1(nums))
