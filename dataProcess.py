from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def is_act_data(x):
    return "motor2" in x


def is_time(x):
    return "time is" in x


def extract(x):
    return x[-8:-1]

def extract_time(x):
    return x[-2:-1]


f = open("/home/jumorean/桌面/data1111.txt")
lst = f.readlines()

act_num = list(filter(is_act_data, lst))
# time = list(filter(is_time, lst))
num = list(map(extract, act_num))
# real_time = list(map(extract_time, time))

# for item in lst:
#     if "100" not in item and item != '':
#         num.append(item[10:-1])
#         # print(item[-7: -1])

num = list(map(int, num))
# time = list(map(float, real_time))
act_arr = np.array(num)
act_arr = act_arr[500:]

# time_arr = np.array(time)
# time = np.linspace(0, (len(act_arr)-1)*0.05, len(act_arr))
# diff_y = pd.DataFrame(act_arr).diff()
# act_arr = act_arr[50:]
# act_arr = act_arr - 13107200
# time = time[50:]
# print(num)
# print("len = ", len(act_arr))
# plt.plot(time, act_arr)

# diff_y = diff_y[0:20]
# time = time[0:20]
# zeros = np.linspace(0, 0, len(act_arr))
# print(len(diff_y))
# print(len(zeros))

# plt.plot(act_arr)
plt.xlabel("time/second")
# plt.plot(time, zeros)
plt.ylabel("position - positionOutput()")

print(act_arr.max())
print(len(act_arr))
plt.legend(["relPos", "zero"], loc='upper left')
plt.grid(True)
plt.plot(act_arr)
# plt.plot(diff_y)
plt.show()






