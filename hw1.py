import pandas as pd
from minPriorityQueue import minPriorityQueue as mPQ


def main():
    # header ：指定作為列名的行，預設0，即取第一行，資料為列名行以下的資料；若資料不含列名，則設定 header = None；
    df = pd.read_excel('test instance.xlsx', header=None)
    process_time = df.iloc[0, 1:].tolist()
    print(process_time)
    arrival_time = df.iloc[1, 1:].tolist()
    print(arrival_time)


main()
