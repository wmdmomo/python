import numpy as np


# load data from txt
def load():
    data_set = []
    data_label = []
    file = open('data.txt')  # 读取数据
    for line in file:
        line = line.strip('\n').split(' ')
        for i in range(len(line)):
            line[i] = float(line[i])
        data_set.append(line[0:2])
        data_label.append(int(line[2]))
    file.close()
    data = np.array(data_set)
    label = np.array(data_label)
    return data, label


def plotdata(data, label):
    neg = np.where(label == -1)
    pos = np.where(label == 1)

    pos_data = []
    neg_data = []

    for i in range(len(pos[0])):
        pos_data.append(data[pos[0][i]])
    for j in range(len(neg[0])):
        neg_data.append(data[neg[0][j]])
    pos_data = np.array(pos_data)
    neg_data = np.array(neg_data)
    return pos_data, neg_data
