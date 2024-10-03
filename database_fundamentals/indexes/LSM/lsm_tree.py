class LSMTree:
    def __init__(self, memtable_limit=5):
        self.memtable = {}
        self.sstables = []
        self.memtable_limit = memtable_limit

    def insert(self, key, value):
        self.memtable[key] = value
        if len(self.memtable) >= self.memtable_limit:
            self.flush_memtable()

    def flush_memtable(self):
        # Flush memtable to a new SSTable
        self.sstables.append(self.memtable)
        self.memtable = {}
        self.compact_sstables()

    def search(self, key):
        # Search in memtable
        if key in self.memtable:
            return self.memtable[key]
        
        # Search in SSTables
        for sstable in reversed(self.sstables):
            if key in sstable:
                return sstable[key]
        
        return None

    def delete(self, key):
        self.memtable[key] = None
        if len(self.memtable) >= self.memtable_limit:
            self.flush_memtable()

    def compact_sstables(self):
        # Simple compaction: merge all SSTables into one
        if len(self.sstables) > 1:
            merged_sstable = {}
            for sstable in self.sstables:
                merged_sstable.update(sstable)
            self.sstables = [merged_sstable]

# Example usage
lsm_tree = LSMTree()
lsm_tree.insert('key1', 'value1')
lsm_tree.insert('key2', 'value2')
lsm_tree.insert('key3', 'value3')
lsm_tree.insert('key4', 'value4')
lsm_tree.insert('key5', 'value5')  # This will trigger a flush
print(lsm_tree.search('key1'))  # Output: value1
lsm_tree.delete('key1')
print(lsm_tree.search('key1'))  # Output: None