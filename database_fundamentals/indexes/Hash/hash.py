class HashIndex:
    def __init__(self, initial_capacity=8, load_factor=0.75):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.index = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_index = self.index
        self.capacity *= 2
        self.index = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_index:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        if self.size / self.capacity > self.load_factor:
            self._resize()

        hashed_key = self._hash(key)
        bucket = self.index[hashed_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

    def search(self, key):
        hashed_key = self._hash(key)
        bucket = self.index[hashed_key]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        hashed_key = self._hash(key)
        bucket = self.index[hashed_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

# Example usage
hash_index = HashIndex()
hash_index.insert('key1', 'value1')
hash_index.insert('key2', 'value2')
print(hash_index.search('key1'))  # Output: value1
print(hash_index.search('key2'))  # Output: value2
hash_index.delete('key1')
print(hash_index.search('key1'))  # Output: None