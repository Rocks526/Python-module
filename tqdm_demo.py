# tqdm示例 Python进度条

from tqdm import tqdm, trange
import time

# tqdm(list)方法可以传入任意一种list
for i in tqdm(range(100)):
    # 每0.5秒增加1%
    time.sleep(0.5)

for char in tqdm(['a', 'b', 'c', 'd', 'e']):
    # 每0.5秒到下一个元素 展示的进度条是百分数
    print(char)
    time.sleep(0.5)

# tqdm(range(100))  等价于  trange(100)
for i in trange(100):
    pass

# desc描述信息 mininterval是进度条展示间隔 每n秒打印一次 initial是初始值
for i in tqdm(iterable=range(100), desc="Process", mininterval=3, initial=20):
    time.sleep(1)
    print(i)
