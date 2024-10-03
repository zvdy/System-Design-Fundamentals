class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.leaf = leaf  # True if node is a leaf, otherwise False
        self.keys = []  # List to store keys
        self.children = []  # List to store child nodes
        self.t = t  # Minimum degree (defines the range for number of keys)

    def insert_non_full(self, key):
        if self.leaf:
            # If node is a leaf, insert the key in the correct position
            self.keys.append(key)
            self.keys.sort()
        else:
            # If node is not a leaf, find the child which is going to have the new key
            i = len(self.keys) - 1
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            # If the found child is full, split it
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                # After split, the middle key of children[i] goes up and children[i] is split into two
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BPlusTreeNode(t, y.leaf)  # Create a new node which is going to store (t-1) keys of y
        self.children.insert(i + 1, z)  # Insert the new node as a child of this node
        self.keys.insert(i, y.keys[t - 1])  # Move the middle key of y to this node
        z.keys = y.keys[t:(2 * t - 1)]  # Copy the last (t-1) keys of y to z
        y.keys = y.keys[0:(t - 1)]  # Reduce the number of keys in y
        if not y.leaf:
            z.children = y.children[t:(2 * t)]  # Copy the last t children of y to z
            y.children = y.children[0:t]  # Reduce the number of children in y

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(t, True)  # Create the root node
        self.t = t  # Minimum degree

    def insert(self, key):
        root = self.root
        # If root is full, then tree grows in height
        if len(root.keys) == 2 * self.t - 1:
            new_root = BPlusTreeNode(self.t)  # Create a new root
            new_root.children.append(self.root)  # Make old root as child of new root
            new_root.split_child(0)  # Split the old root and move a key to the new root
            self.root = new_root  # Change root
            self.root.insert_non_full(key)  # Insert the key in the new root
        else:
            root.insert_non_full(key)  # If root is not full, call insert_non_full for root

    def search(self, key, node=None):
        if node is None:
            node = self.root
        i = 0
        # Find the first key greater than or equal to key
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        # If the found key is equal to key, return True
        if i < len(node.keys) and key == node.keys[i]:
            return True
        # If the key is not found here and this is a leaf node
        if node.leaf:
            return False
        # Go to the appropriate child
        return self.search(key, node.children[i])

# Example usage
b_plus_tree = BPlusTree(3)
b_plus_tree.insert(10)
b_plus_tree.insert(20)
b_plus_tree.insert(5)
b_plus_tree.insert(6)
b_plus_tree.insert(12)
b_plus_tree.insert(30)
b_plus_tree.insert(7)
b_plus_tree.insert(17)

print(b_plus_tree.search(6))  # Output: True
print(b_plus_tree.search(15)) # Output: False