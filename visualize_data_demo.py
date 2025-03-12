import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)
'''
Matplotlib
用途：matplotlib 是一个用于创建静态、交互式和动画可视化的绘图库。
功能：
提供了一种类似于 MATLAB 的绘图框架。
支持多种图表类型，包括线图、散点图、柱状图、直方图、饼图等。
可以自定义图表的样式、颜色、标签、图例等。
支持保存图表为多种格式，如 PNG、JPEG、PDF、SVG 等。
应用场景：matplotlib 常用于数据可视化、探索性数据分析、结果展示等。
'''
'''
Seaborn
用途：seaborn 是一个基于 matplotlib 的数据可视化库，旨在提供更高级的接口和更美观的默认样式。
功能：
提供了更简洁的语法来创建复杂的图表。
内置了多种统计图表，如分布图、回归图、热图、箱型图等。
提供了更丰富的颜色主题和样式选项。
支持对大数据集进行高效的可视化。
应用场景：seaborn 常用于统计分析、数据探索、结果展示等，特别适合需要展示数据分布和关系的场景。
'''
'''
NumPy
用途：numpy 是一个用于科学计算的基础库，提供了对多维数组的支持和一系列数学函数。
功能：
提供了高效的多维数组对象 ndarray。
支持对数组进行各种数学运算，如加减乘除、矩阵乘法、统计分析等。
提供了广播（broadcasting）机制，可以简化数组运算。
支持线性代数、傅里叶变换、随机数生成等数学函数。
应用场景：numpy 常用于数值计算、数据处理、机器学习、科学模拟等领域，是许多科学计算库（如 scipy、pandas、scikit-learn 等）的基础。
'''
'''
绘制散点图
展示两列之间的关系：
'''
plt.scatter(df['A'], df['B'])
plt.title('Scatter plot of A vs B')
plt.xlabel('A')
plt.ylabel('B')
plt.show()

'''
绘制线图
展示一列随另一列变化的趋势：
'''
plt.plot(df['A'], df['B'])
plt.title('Line plot of B vs A')
plt.xlabel('A')
plt.ylabel('B')
plt.show()

'''
绘制分布图
展示单列的分布情况：
'''
sns.histplot(df['A'], kde=True)
plt.title('Distribution of A')
plt.show()
'''
绘制回归图
展示两列之间的线性关系：
'''
sns.regplot(x='A', y='B', data=df)
plt.title('Regression plot of B vs A')
plt.show()

'''
拟合数据的特征曲线
如果你想要拟合数据的特征曲线，可以使用 numpy 的 polyfit 方法进行多项式拟合：
'''
import numpy as np

# 多项式拟合
coefficients = np.polyfit(df['A'], df['B'], 2)  # 2 表示二次多项式
polynomial = np.poly1d(coefficients)

# 绘制原始数据和拟合曲线
plt.scatter(df['A'], df['B'], label='Data')
plt.plot(df['A'], polynomial(df['A']), color='red', label='Fit')
plt.title('Polynomial Fit of B vs A')
plt.xlabel('A')
plt.ylabel('B')
plt.legend()
plt.show()

''' 保存图表 '''
plt.savefig('plot.png')
