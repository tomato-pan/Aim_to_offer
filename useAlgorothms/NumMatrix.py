# LC304
'''
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 20

'''


class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i][j + 1] = _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_all = 0
        for i in range(row1, row2 + 1):
            sum_all += sum(self.matrix[i][col1:col2 + 1])
        return sum_all

    def sumRegion1(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums

        total = sum(_sums[i][col2 + 1] - _sums[i][col1] for i in range(row1, row2 + 1))
        return total


class NumMatrix1:

    def __init__(self, matrix):
        # # 只有matrix非空才有后面的计算
        # if matrix:
        #     m,n = len(matrix),len(matrix[0])
        #     # 用pre_sum存储以(0,0)为左上角 (i,j)为右下角的子矩阵元素和
        #     self.pre_sum = [[0]*n for _ in range(m)]
        #     self.pre_sum[0][0] = matrix[0][0]
        #     # 依据matrix计算每个位置的数值
        #     for i in range(1,m):
        #         self.pre_sum[i][0] = self.pre_sum[i-1][0] + matrix[i][0]
        #     for i in range(1,n):
        #         self.pre_sum[0][i] = self.pre_sum[0][i-1] + matrix[0][i]
        #     for i in range(1,m):
        #         for j in range(1,n):
        #             self.pre_sum[i][j] = self.pre_sum[i-1][j]+self.pre_sum[i][j-1]+matrix[i][j]-self.pre_sum[i-1][j-1]

        import numpy as np
        # 将矩阵存为numpy.array类型
        self.arr = np.array(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # # 将每个子矩阵分为4个部分计算
        # a = self.pre_sum[row2][col2]
        # b = self.pre_sum[row2][col1-1] if col1 > 0 else 0
        # c = self.pre_sum[row1-1][col2] if row1 > 0 else 0
        # d = self.pre_sum[row1-1][col1-1] if col1 > 0 and row1 > 0 else 0
        # return a - b - c + d

        # 将numpy.int类型转为int类型
        return int(self.arr[row1:row2 + 1, col1:col2 + 1].sum())


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(0, 1, 1, 2))
    print(obj.sumRegion(0, 0, 0, 0))
    print(obj.sumRegion1(0, 0, 0, 1))
    print(obj.sumRegion1(1, 1, 2, 2))
    print(obj.sumRegion1(1, 1, 2, 4))

