import numpy as np
import matplotlib.pyplot as plt
#创建画布并引入axisartist工具。
import mpl_toolkits.axisartist as axisartist
# 绘制椭圆曲线
def main():
    a = 0
    b = 7
    fig = plt.figure(figsize=(6, 6))
    ax = axisartist.Subplot(fig, 111)
    # 将绘图区对象添加到画布中
    fig.add_axes(ax)
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    ax.axis[:].set_visible(False)  # 通过set_visible方法设置绘图区所有坐标轴隐藏
    ax.axis["x"] = ax.new_floating_axis(0, 0)  # ax.new_floating_axis代表添加新的坐标轴
    ax.axis["x"].set_axisline_style("->", size=1.0)  # 给x坐标轴加上箭头
    # 添加y坐标轴，且加上箭头
    ax.axis["y"] = ax.new_floating_axis(1, 0)
    ax.axis["y"].set_axisline_style("-|>", size=1.0)
    # 设置x、y轴上刻度显示方向
    ax.axis["x"].set_axis_direction("top")
    ax.axis["y"].set_axis_direction("right")
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()