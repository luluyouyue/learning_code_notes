#-*- coding=utf-8 -*-
import sys
import pandas as pd
import numpy as np
"""
机器学习流程：
1、读取数据
2、提取特征
3、将特征转化为numpy数组
4、训练
"""

d = {'a': [1, 2], 'b': [4, 5], 'label': [1, 0]}

# 读取数据，我这是自己创建的，可以从csv中读取
df = pd.DataFrame(data=d)

# 按行创建行
def handle_row(row):
    f = [['a', 'b']]
    return f

def handle_row2(row):
    f = [['c', 'd']]
    return f

df['ab'] = df.apply(handle_row, axis=1)
print(df)

df['cd'] = df.apply(handle_row2, axis=1)
print(df)


# 合并行
def merge_feature(row):
    fs = []
    for feature in ['ab', 'cd']:
        fs += row[feature][0]
    return fs


df["feature"] = df.apply(merge_feature, axis=1)
print(df)

# 将特征转化为np数组以供训练
x, y = np.array(df["feature"].tolist()), np.array(df["label"].astype(int))
print('x = ', x, 'y = ', y)

