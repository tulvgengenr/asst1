import matplotlib.pyplot as plt

# 定义 x 轴和 y 轴的数据
x = [2, 3, 4, 5, 6, 8, 10, 12, 24, 48, 80, 100, 120, 150]
y = [1.72, 1.59, 1.83, 2.18, 2.64, 3.38, 4.04, 4.38, 5.47, 6.22, 7.28, 7.72, 7.54, 7.30]

# 绘制折线图
plt.plot(x, y, marker='o')

# 设置图表标题和轴标签
plt.title('')
plt.xlabel('threads number')
plt.ylabel('speed up')

# 保存图表到本地文件
plt.savefig('report1.png')

# 显示图表
plt.show()
