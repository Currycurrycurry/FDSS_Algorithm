# 【attention算子】numpy实现
import numpy as np
from numpy.random import randn

d = 256 #dimension
n = 32 #32个序列
x = randn(d,n) # 256 * 32
print(x.shape) # (256, 32)

w_q = randn(d,d)
w_k = randn(d,d)
w_v = randn(d,d)

q = w_q @ x
k = w_k @ x
v = w_v @ x

print(q.shape) # (256, 32)

def softmax(x):
    e_x = np.exp(x-np.max(x))# 防溢出
    return e_x/e_x.sum(axis=0)

# 先计算q和k之间的点乘，然后除一个尺度标度防止结果过大
output = v @ softmax(k.T @ q / np.sqrt(d))

# 【attention算子】torch实现
from math import sqrt
import torch
import torch.nn as nn

# Self-Attention 机制的实现
class Self_Attention(nn.Module):
    # input : batch_size * seq_len * input_dim
    def __init__(self,input_dim,dim_k,dim_v):
        super(Self_Attention,self).__init__()
        self.q = nn.Linear(input_dim,dim_k) # q : batch_size * input_dim * dim_k
        self.k = nn.Linear(input_dim,dim_k) # k : batch_size * input_dim * dim_k
        self.v = nn.Linear(input_dim,dim_v) # v : batch_size * input_dim * dim_v
        self._norm_fact = 1 / sqrt(dim_k)

    def forward(self,x):
        Q = self.q(x) # Q: batch_size * seq_len * dim_k
        K = self.k(x) # K: batch_size * seq_len * dim_k
        V = self.v(x) # V: batch_size * seq_len * dim_v
        # K.permute(0,2,1)# 将K的维度索引1和维度索引2交换位置
        # torch.bmm# 两个tensor的矩阵乘法
        atten = nn.Softmax(dim=-1)(torch.bmm(Q,K.permute(0,2,1))) * self._norm_fact # Q * K.T() # batch_size * seq_len * seq_len
        output = torch.bmm(atten,V) # Q * K.T() * V # batch_size * seq_len * dim_v
        return output
