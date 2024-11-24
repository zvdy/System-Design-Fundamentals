class FIFOCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = {}
        self.order = []

    def put(self, key, value):
        if key in self.cache:
            # Update the value and move the key to the end of the order list
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.max_size:
                # Evict the oldest item
                oldest_key = self.order.pop(0)
                del self.cache[oldest_key]
            # Add the new item
            self.cache[key] = value
            self.order.append(key)

    def get(self, key):
        return self.cache.get(key, None)

    def __str__(self):
        return str(self.cache)

# Example usage
if __name__ == "__main__":
    fifo_cache = FIFOCache(3)
    fifo_cache.put(1, 'A')
    fifo_cache.put(2, 'B')
    fifo_cache.put(3, 'C')
    print(fifo_cache)  # Output: {1: 'A', 2: 'B', 3: 'C'}
    fifo_cache.put(4, 'D')
    print(fifo_cache)  # Output: {2: 'B', 3: 'C', 4: 'D'}
    print(fifo_cache.get(2))  # Output: 'B'
    print(fifo_cache.get(1))  # Output: None