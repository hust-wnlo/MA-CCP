import sys
sys.path.append("../")
from algs.lib.heapdict import HeapDict
from algs.lib.cacheop import CacheOp


class LFU:
    class LFU_Entry:
        def __init__(self, oblock, freq=1, time=0):
            self.oblock = oblock
            self.freq = freq
            self.time = time

        def __lt__(self, other):
            if self.freq == other.freq:
                return self.time > other.time
            return self.freq < other.freq

        def __repr__(self):
            # return "(o={}, f={}, t={})".format(self.oblock, self.freq,
            #                                    self.time)
            return str(self.freq)

    def __init__(self, cache_size, window_size, **kwargs):
        self.cache_size = cache_size
        self.lfu = HeapDict()
        self.time = 0


    def __contains__(self, oblock):
        return oblock in self.lfu

    def cacheFull(self):
        return len(self.lfu) == self.cache_size

    def addToCache(self, oblock):
        x = self.LFU_Entry(oblock, freq=1, time=self.time)
        self.lfu[oblock] = x

    def hit(self, oblock):
        x = self.lfu[oblock]
        x.freq += 1
        x.time = self.time
        self.lfu[oblock] = x

    def evict(self):
        lfu_min = self.lfu.popMin()
        return lfu_min.oblock

    def miss(self, oblock):
        evicted = None

        # print("request: " + str(oblock))
        # print(self.lfu)

        if len(self.lfu) == self.cache_size:
            evicted = self.evict()
        self.addToCache(oblock)

        return evicted

    def request(self, oblock, ts):
        miss = True
        evicted = None
        op = CacheOp.INSERT

        self.time += 1

        if oblock in self:
            miss = False
            op = CacheOp.HIT
            self.hit(oblock)
        else:
            evicted = self.miss(oblock)

        return op, evicted


if __name__ == '__main__':
    LFU = LFU_CR(5, 10)
    LFU.request(3, 0)
    LFU.request(1, 0)
    LFU.request(5, 0)
    LFU.request(6, 0)
    LFU.request(2, 0)
    LFU.request(3, 0)
    LFU.request(8, 0)
    print(LFU.lfu)
    LFU.request(9, 0)
    print(LFU.lfu)



from .lib.dequedict import DequeDict
from .lib.cacheop import CacheOp


class LRU:
    class LRU_Entry:
        def __init__(self, oblock):
            self.oblock = oblock

        def __repr__(self):
            return "(o={})".format(self.oblock)

    def __init__(self, cache_size, window_size, **kwargs):
        self.cache_size = cache_size

        self.lru = DequeDict()

        self.time = 0


    def __contains__(self, oblock):
        return oblock in self.lru

    def cacheFull(self):
        return len(self.lru) == self.cache_size

    def addToCache(self, oblock):
        x = self.LRU_Entry(oblock)
        self.lru[oblock] = x

    def hit(self, oblock):
        x = self.lru[oblock]
        self.lru[oblock] = x

    def evict(self):
        lru = self.lru.popFirst()
        return lru.oblock

    def miss(self, oblock):
        evicted = None

        if len(self.lru) == self.cache_size:
            evicted = self.evict()
        self.addToCache(oblock)

        return evicted

    def request(self, oblock, ts):
        miss = True
        evicted = None

        self.time += 1

        if oblock in self:
            miss = False
            self.hit(oblock)
        else:
            evicted = self.miss(oblock)

        op = CacheOp.INSERT if miss else CacheOp.HIT

        return op, evicted













