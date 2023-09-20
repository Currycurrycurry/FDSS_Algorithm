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

# 手写梯度下降
import numpy as np
def gradient_decsent(input_data, iteration_rounds, learning_rate):
    # initialize the x 
    X = np.rand(0, 1)
    # do gd 
    for _ in range(iteration_rounds):
        for a, b in input_data: # or mini-batch 
            delta_x = np.dot(np.reverse(a), b) 
            X -= learning_rate * delta_x
    return X

# 【交叉熵反向传播推导】

def softmax(x, dim=1):
    x = x - torch.max(x, dim=dim)[0].unsqueeze(dim=dim) # 防止溢出
    res = torch.exp(x) / torch.sum(torch.exp(x), dim=dim).unsqueeze(dim=dim)
    return res

# seed_torch(1234)
x=torch.rand(4,7, requires_grad=True)  # 4个样本，共7类
y=torch.LongTensor([1,3,5,0]) # 对应的标签
criterion = torch.nn.CrossEntropyLoss()  # pytroch库
out = criterion(x,y)
print(out)
# 自己实现
gt = torch.zeros(4,7).scatter(1, y.view(4,1),1)  # 生成one-hot标签，scatter的用法可参考jianshu.com/p/b4e9fd4048f4
loss = -(torch.log(softmax(x, dim=-1)) * gt).sum() / 4  # 对样本求平均
print(loss)

if __name__ == '__main__':
    seed_torch(1234)
    x=torch.rand(4,7, requires_grad=True)

    print(torch.softmax(x,dim=-1))
    print(softmax(x, dim=-1))
    
# 手写多线程矩阵相乘
import numpy as np
from scipy.sparse import random
from scipy.sparse.linalg import spsolve
from threading import Thread

# Function to perform sparse matrix multiplication
def sparse_matrix_multiply(sparse_matrix, dense_matrix, result_queue):
    result = sparse_matrix.dot(dense_matrix)
    result_queue.put(result)

# Create a sparse matrix
num_rows = 1000
num_cols = 1000
sparsity = 0.1
sparse_matrix = random(num_rows, num_cols, density=sparsity, format='csr')

# Create a dense matrix
dense_matrix = np.random.rand(num_cols, num_cols)

# Number of threads
num_threads = 4

# Split the rows for each thread
rows_per_thread = num_rows // num_threads

# Create a queue to hold the results
result_queue = Queue()

# Create and start threads
threads = []
for i in range(num_threads):
    start_row = i * rows_per_thread
    end_row = (i + 1) * rows_per_thread if i < num_threads - 1 else num_rows
    thread = Thread(target=sparse_matrix_multiply, args=(sparse_matrix[start_row:end_row], dense_matrix, result_queue))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Collect and combine results from the queue
final_result = np.vstack([result_queue.get() for _ in range(num_threads)])

print(final_result)

# 系统启动一个新线程的成本是比较高的，因为它涉及与操作系统的交互。
# 在这种情形下，使用线程池可以很好地提升性能，尤其是当程序中需要创建大量生存期很短暂的线程时，更应该考虑使用线程池。
# 线程池在系统启动时即创建大量空闲的线程，程序只要将一个函数提交给线程池，线程池就会启动一个空闲的线程来执行它。
# 当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成空闲状态，等待执行下一个函数。

# 此外，使用线程池可以有效地控制系统中并发线程的数量。
# 当系统中包含有大量的并发线程时，会导致系统性能急剧下降，甚至导致 Python 解释器崩溃，
# 而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数。

# 【手写基于线程池的多线程矩阵相乘】

import numpy as np
from scipy.sparse import random
from concurrent.futures import ThreadPoolExecutor

# Function to perform sparse matrix multiplication
def sparse_matrix_multiply(sparse_matrix, dense_matrix):
    result = sparse_matrix.dot(dense_matrix)
    return result

# Create a sparse matrix
num_rows = 1000
num_cols = 1000
sparsity = 0.1
sparse_matrix = random(num_rows, num_cols, density=sparsity, format='csr')

# Create a dense matrix
dense_matrix = np.random.rand(num_cols, num_cols)

# Number of threads in the thread pool
num_threads = 4

# Create a thread pool
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Split the rows for each thread
    rows_per_thread = num_rows // num_threads
    
    # Submit tasks to the thread pool
    future_to_row = {}
    for i in range(num_threads):
        start_row = i * rows_per_thread
        end_row = (i + 1) * rows_per_thread if i < num_threads - 1 else num_rows
        future = executor.submit(sparse_matrix_multiply, sparse_matrix[start_row:end_row], dense_matrix)
        future_to_row[future] = (start_row, end_row)
    
    # Wait for the tasks to complete and collect results
    final_result = np.zeros((num_rows, num_cols))
    for future in concurrent.futures.as_completed(future_to_row):
        start_row, end_row = future_to_row[future]
        result = future.result()
        final_result[start_row:end_row] = result

print(final_result)

# 无锁环形缓存器RingBuffer

import threading

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0
        self.full_event = threading.Event()
        self.empty_event = threading.Event()
        self.lock = threading.Semaphore(1)
    
    def put(self, item):
        self.empty_event.clear()
        
        self.lock.acquire()
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity
        self.count += 1
        
        if self.count == self.capacity:
            self.full_event.set()
        
        self.lock.release()
    
    def get(self):
        self.full_event.clear()
        
        self.lock.acquire()
        item = self.buffer[self.tail]
        self.tail = (self.tail + 1) % self.capacity
        self.count -= 1
        
        if self.count == 0:
            self.empty_event.set()
        
        self.lock.release()
        
        return item
    
    def is_full(self):
        return self.count == self.capacity
    
    def is_empty(self):
        return self.count == 0

# Example usage
def producer(rb, start, end):
    for i in range(start, end):
        rb.put(i)

def consumer(rb, num_items):
    for _ in range(num_items):
        item = rb.get()
        print(f"Consumed: {item}")

buffer_capacity = 10
ring_buffer = RingBuffer(buffer_capacity)

producer_thread = threading.Thread(target=producer, args=(ring_buffer, 0, 20))
consumer_thread = threading.Thread(target=consumer, args=(ring_buffer, 20))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()