from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.cache = {}
        self.freq = defaultdict(list)
        self.key_freq = {}

    def _update_freq(self, key):
        freq = self.key_freq[key]
        self.freq[freq].remove(key)
        if not self.freq[freq]:
            del self.freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_freq[key] += 1
        self.freq[self.key_freq[key]].append(key)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._update_freq(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = value
            self._update_freq(key)
        else:
            if len(self.cache) >= self.capacity:
                evict_key = self.freq[self.min_freq].pop(0)
                if not self.freq[self.min_freq]:
                    del self.freq[self.min_freq]
                del self.cache[evict_key]
                del self.key_freq[evict_key]

            self.cache[key] = value
            self.key_freq[key] = 1
            self.freq[1].append(key)
            self.min_freq = 1

# Example usage
lfu_cache = LFUCache(2)
lfu_cache.put(1, 1)
lfu_cache.put(2, 2)
print(lfu_cache.get(1))  # returns 1
lfu_cache.put(3, 3)      # evicts key 2
print(lfu_cache.get(2))  # returns -1 (not found)
print(lfu_cache.get(3))  # returns 3
lfu_cache.put(4, 4)      # evicts key 1
print(lfu_cache.get(1))  # returns -1 (not found)
print(lfu_cache.get(3))  # returns 3
print(lfu_cache.get(4))  # returns 4