import pandas as pd
from minPriorityQueue import minPriorityQueue as mPQ


def SRPT(process_time, arrival_time):
    current_time = 0
    process_queue = mPQ()
    for i in range(len(arrival_time)):
        if arrival_time[i] <= current_time:
            process_queue.insert(process_time[i])
            print("{} round, and heap is {}, current_time = {}".format(
                i, process_queue.heap, current_time))
            if i != (len(arrival_time) - 1):
                can_use_time = arrival_time[i + 1] - arrival_time[i]
                try:
                    while can_use_time >= process_queue.heap[1]:
                        # 可以執行目前剩餘時間最小的process
                        min_time = process_queue.extractMin()
                        current_time += min_time
                        can_use_time -= min_time
                    process_queue.heap[1] -= can_use_time
                    current_time += can_use_time
                except:
                    print("{} round, and heap is {}, current_time = {}".format(
                        i, process_queue.heap, current_time))
                    print("error")
            else:
                # 最後一個process已進入heap，只要把heap內的值加總即可知道總完工時間
                del process_queue.heap[0]
                current_time += sum(process_queue.heap)
        else:
            print("{} round, and heap is {}, current_time = {}".format(
                i, process_queue.heap, current_time))
            # arrival_time > current_time
            can_use_time = arrival_time[i] - current_time
            if len(process_queue.heap) == 1:
                current_time += can_use_time
            else:
                while can_use_time >= process_queue.heap[1]:
                    # 可以執行目前剩餘時間最小的process
                    min_time = process_queue.extractMin()
                    current_time += min_time
                    can_use_time -= min_time
                process_queue.heap[1] -= can_use_time
                current_time += can_use_time
            # 因為已經有等時間了，所以最後還是得把process time加回去
            process_queue.insert(process_time[i])

    print("completion time = {}".format(
        current_time))


def main():
    # header ：指定作為列名的行，預設0，即取第一行，資料為列名行以下的資料；若資料不含列名，則設定 header = None；
    df = pd.read_excel('test instance.xlsx', header=None)
    process_time = df.iloc[0, 1:].tolist()
    print(process_time)
    arrival_time = df.iloc[1, 1:].tolist()
    print(arrival_time)

    SRPT(process_time[:20], arrival_time[:20])


main()
