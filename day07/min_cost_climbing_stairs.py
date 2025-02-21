"""
LCR 088. 使用最小花费爬楼梯
    数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
    每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。
    请找出达到楼层顶部的最低花费。
    在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
    示例 1：
            输入：cost = [10, 15, 20]
            输出：15
            解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
     示例 2：
            输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
            输出：6
            解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
"""
from typing import List

"""
核心思想：
    到达每个阶梯 i 的最小花费等于从阶梯 i-1 或 i-2 中
    选择一个花费较小的，再加上当前阶梯的花费。
"""


# 方法一：
def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    # 我们定义 dp[i] 表示达到第 i 个位置的最小花费
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]


# 方法二：空间优化
def minCostClimbingStairs1(cost):
    n = len(cost)
    # dp0 和 dp1 分别表示到达前两个阶梯的最小花费（起始位置不花费）
    dp0, dp1 = 0, 0
    for i in range(2, n + 1):
        dp0, dp1 = dp1, min(dp1 + cost[i - 1], dp0 + cost[i - 2])
    return dp1


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))
