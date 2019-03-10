#!usr/bin/env python3
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import csv

data_dict = {}
data_list = []
with open('data_tokyo.csv') as f:
    # csv ファイルを読み込む
    reader = csv.reader(f)
    
    # ヘッダー部分を読み飛ばす
    for _ in range(6):
        next(reader)
        
    for row in reader:
        data_dict[str(row[0])] = float(row[1])
        data_list.append(float(row[1]))

# ndarray へ変換
data_list = np.array(data_list)

#mean = data_list.sum()/len(data_list)
mean = data_list.mean()
#std  = np.sqrt(((data_list - mean)**2).sum()/len(data_list))
std = data_list.std()

print('平均気温の平均値:{:.4f}'.format(mean))
print('平均気温の標準偏差:{:.4f}'.format(std))

data_mean = []
for i in range(len(data_list) - 11):
    data_mean.append(np.average(data_list[i:i+12]))
    

plt.plot(data_mean)
plt.show()
