"""
LCR 041. 数据流中的移动平均值
    给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。
    实现 MovingAverage 类：
    MovingAverage(int size) 用窗口大小 size 初始化对象。
    double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，
    请计算并返回数据流中最后 size 个值的移动平均值，即滑动窗口里所有数字的平均值。
    示例：
        输入：
            inputs = ["MovingAverage", "next", "next", "next", "next"]
            inputs = [[3], [1], [10], [3], [5]]
        输出：[null, 1.0, 5.5, 4.66667, 6.0]
        解释：
            MovingAverage movingAverage = new MovingAverage(3);
            movingAverage.next(1); // 返回 1.0 = 1 / 1
            movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
            movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
            movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3
"""
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.total = 0

    # def next(self, val: int) -> float:
    #     self.queue.append(val)
    #     while len(self.queue) > self.size:
    #         self.queue.popleft()
    #     return sum(self.queue) / len(self.queue)

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.total -= self.queue.popleft()
        self.queue.append(val)
        self.total += val
        return self.total / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
