import numpy as np
import matplotlib.pyplot as plt
import tool

# load data from txt
data = tool.load()[0]
label = tool.load()[1]

w = np.array([0, 0])
b = 0
n = 1
f = (np.dot(data, w.T) + b) * label
id = np.where(f <= 0)
time = 1
print('迭代次数\t误分类点\tw\tb\tw*x+b\t')
while id[0].size > 0:
    point = np.random.randint(0, id[0].size)  # 生成一个随机数，任意选取一个点
    w = w + n * label[id[0][point]] * data[id[0][point]]
    b = b + n * label[id[0][point]]
    print('%d\tx%d\t(%d,%d)T\t%d\t%dx(1)+%dx(2)+%d' % (time, id[0][point] + 1, w[0], w[1], b, w[0], w[1], b))
    f = (np.dot(data, w.T) + b) * label
    id = np.where(f <= 0)
    time += 1

pos_data = tool.plotdata(data, label)[0]
neg_data = tool.plotdata(data, label)[1]

plt.plot(pos_data[:, 0], pos_data[:, 1], 'ro')
plt.plot(neg_data[:, 0], neg_data[:, 1], 'bo')
x1 = np.arange(0, 10, 0.1)
if w[1] != 0:
    x2 = (w[0] * x1 + b) / (-w[1])
    plt.plot(x1, x2)
else:
    xx = -b / w[0]
    plt.vlines(xx, 0, 10)
plt.axis([0, 10, 0, 10])

plt.show()
