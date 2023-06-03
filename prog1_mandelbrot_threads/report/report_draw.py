import matplotlib.pyplot as plt

# 定义 x 轴和 y 轴的数据
x0 = [2, 3, 4, 5, 6, 8, 10]
y0 = [1.72, 1.59, 1.83, 2.18, 2.64, 3.38, 4.04]

x1 = [2, 3, 4, 5, 6, 10]
y1 = [1.67, 1.99, 2.06, 2.21, 2.80, 3.85]
# 绘制折线图
fig, ax = plt.subplots()
plt.plot(x0, y0, marker='o', label='view1')
plt.plot(x1, y1, marker='o', label='view2')

# 设置图表标题和轴标签
plt.title('')
plt.xlabel('threads number')
plt.ylabel('speed up')

ax.legend()
# 保存图表到本地文件
plt.savefig('report1.png')

# 显示图表
plt.show()
