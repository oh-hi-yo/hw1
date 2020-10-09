class minPriorityQueue:
    # implement a minimmum priority queue by min heap
    def __init__(self):
        self.heap = list([None])  # None for the heap[0], root = heap[1]
        self.length = 0
        return

    def insert(self, item):
        # insert item to the end then swim it up
        self.heap.append(item)
        self.length = self.length + 1
        self.__swim(self.length)
        return

    def extractMin(self):
        # exchange first item and last item, then order again
        minimum = self.heap[1]
        self.__exchange(1, self.length)
        # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        self.heap.pop()
        self.length = self.length - 1
        #print("the extractMin heap length = {}". format(self.length))
        self.__sink(1)
        #print("the extractMin heap is {}".format(self.heap))
        return minimum

    # __swim() 等前面有兩個底線的函數，也像是 C 或 Java 等語言中的 private 作用，能夠限制函數只能在類別中被呼叫
    def __swim(self, k):
        # Exchange key in child with key in parent. Repeat until heap order restored.
        while k > 1 and self.__more(k // 2, k):
            self.__exchange(k // 2, k)
            k = k // 2
            #print("swim k = {}".format(k))
        return

    def __sink(self, k):
        # Key in parent exchange with key in smaller child. Repeat until heap order restored.
        while k * 2 <= self.length:
            j = k * 2
            if j < self.length and self.__more(j, j + 1):
                j = j + 1
            #print("sink k = {}, j = {}".format(k, j))

            if self.__more(k, j):
                self.__exchange(k, j)  # exchange with the smallest child
            k = j
        return

    def __more(self, a, b):
        # return a boolean represent if item at a position is larger than item at b
        if self.heap[a] > self.heap[b]:
            '''
            print("left is {}, right is {}".format(
                self.heap[a], self.heap[b]))
            '''
            return True
        else:
            return False

    def __exchange(self, a, b):
        # swap item in the heap at position a and b
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
        return
