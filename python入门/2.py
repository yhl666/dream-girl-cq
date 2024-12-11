import matplotlib.pyplot as plt
import numpy as np

# 绘制一个 3D 曲面图
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
z = np.sin(x) * np.cos(y)

# 绘制曲面图
plt.plot_wireframe(x, y, z)

# 添加标题
plt.title("3D 曲面图")

# 添加 x 轴、y 轴和 z 轴标签
plt.xlabel("x")
plt.ylabel("y")
plt.zlabel("z")

# 显示图形
plt.show()
