import tool
import numpy as np
import matplotlib.pyplot as plt
#ceshi
data = tool.load()[0]
label = tool.load()[1]

gram = np.dot(data, data.T)
num = data.shape[0]
a = np.zeros(num)
b = 0
n = 1
gram_ = gram * label * a
gram_new = (gram_.sum(axis=1) + b) * label
id = np.where(gram_new <= 0)
time = 1
print('time\tselect\t', end='')
for i in range(num):
    print('a%d\t' % (i + 1), end='')
print('b\t')
while id[0].size > 0:
    point = np.random.randint(0, id[0].size)  # 生成一个随机数，任意选取一个点
    a[id[0][point]] = a[id[0][point]] + n
    b = b + n * label[id[0][point]]
    print('%d\t' % time, end='')
    print('x(%d)\t' % (id[0][point] + 1), end='')
    for i in range(num):
        print('%d\t' % a[i], end='')
    print('%d\t' % b)
    gram_ = gram * label * a
    gram_new = (gram_.sum(axis=1) + b) * label
    id = np.where(gram_new <= 0)
    time += 1

pos_data = tool.plotdata(data, label)[0]
neg_data = tool.plotdata(data, label)[1]

plt.plot(pos_data[:, 0], pos_data[:, 1], 'ro')
plt.plot(neg_data[:, 0], neg_data[:, 1], 'bo')
x1 = np.arange(0, 10, 0.1)
a_ = a * label
w = np.dot(a_, data)
if w[1] != 0:
    x2 = (w[0] * x1 + b) / (-w[1])
    plt.plot(x1, x2)
else:
    xx = -b / w[0]
    plt.vlines(xx, 0, 10)
plt.axis([0, 10, 0, 10])
plt.show()
