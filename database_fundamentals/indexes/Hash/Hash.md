### Step-by-Step Drawing

1. **Initialization**
    - Create an instance of [`HashIndex`] with an initial capacity of 8 and a load factor of 0.75.
    - Initialize the [`index`] with 8 empty buckets.

2. **Insert 'key1' with 'value1'**
    - Compute the hash of 'key1' and determine the bucket index.
    - Insert ('key1', 'value1') into the appropriate bucket.
    - Increment the size of the hash table.

3. **Insert 'key2' with 'value2'**
    - Compute the hash of 'key2' and determine the bucket index.
    - Insert ('key2', 'value2') into the appropriate bucket.
    - Increment the size of the hash table.

4. **Search for 'key1'**
    - Compute the hash of 'key1' and determine the bucket index.
    - Search the bucket for 'key1' and return 'value1'.

5. **Search for 'key2'**
    - Compute the hash of 'key2' and determine the bucket index.
    - Search the bucket for 'key2' and return 'value2'.

6. **Delete 'key1'**
    - Compute the hash of 'key1' and determine the bucket index.
    - Search the bucket for 'key1' and remove it.
    - Decrement the size of the hash table.

7. **Search for 'key1' after deletion**
    - Compute the hash of 'key1' and determine the bucket index.
    - Search the bucket for 'key1' and return [`None`] since it has been deleted.

### Example Diagrams

#### Initialization
```plaintext
HashIndex
+-------------------+
| capacity: 8       |
| load_factor: 0.75 |
| size: 0           |
| index: [[], [], [], [], [], [], [], []] |
+-------------------+
```

#### Insert 'key1' with 'value1'
```plaintext
HashIndex
+-------------------+
| capacity: 8       |
| load_factor: 0.75 |
| size: 1           |
| index: [[('key1', 'value1')], [], [], [], [], [], [], []] |
+-------------------+
```

#### Insert 'key2' with 'value2'
```plaintext
HashIndex
+-------------------+
| capacity: 8       |
| load_factor: 0.75 |
| size: 2           |
| index: ('key1', 'value1')], [], [], [], [('key2', 'value2')], [], [], []] |
+-------------------+
```

#### Search for 'key1'
```plaintext
Search 'key1'
+-------------------+
| Hash: 0           |
| Bucket: [('key1', 'value1')] |
| Result: 'value1'  |
+-------------------+
```

#### Search for 'key2'
```plaintext
Search 'key2'
+-------------------+
| Hash: 4           |
| Bucket: [('key2', 'value2')] |
| Result: 'value2'  |
+-------------------+
```

#### Delete 'key1'
```plaintext
Delete 'key1'
+-------------------+
| Hash: 0           |
| Bucket: []        |
| Result: True      |
+-------------------+
```

#### Search for 'key1' after deletion
```plaintext
Search 'key1'
+-------------------+
| Hash: 0           |
| Bucket: []        |
| Result: None      |
+-------------------+
```
## Diagram
```mermaid
graph TD
    A[HashIndex]
    A --> B[__init__ initial_capacity=8, load_factor=0.75]
    B --> B1[Initialize capacity, load_factor, size]
    B --> B2[Create index with empty buckets]

    A --> E[insert key, value]
    E --> E1[If size/capacity > load_factor, call _resize]
    E1 --> E2[_resize]
    E2 --> E3[Double the capacity]
    E2 --> E4[Rehash all existing key-value pairs]
    E --> E5[Compute hashed_key using _hash key]
    E --> E6[Get bucket at index hashed_key]
    E --> E7[For each k, v in bucket]
    E7 --> E8[If k == key, update value and return]
    E --> E9[Append key, value to bucket]
    E --> E10[Increment size]

    A --> F[search key]
    F --> F1[Compute hashed_key using _hash key]
    F --> F2[Get bucket at index hashed_key]
    F --> F3[For each k, v in bucket]
    F3 --> F4[If k == key, return value]
    F --> F5[Return None if key not found]

    A --> G[delete key]
    G --> G1[Compute hashed_key using _hash key]
    G --> G2[Get bucket at index hashed_key]
    G --> G3[For each k, v in bucket]
    G3 --> G4[If k == key, delete k, v from bucket]
    G4 --> G5[Decrement size]
    G4 --> G6[Return True]
    G --> G7[Return False if key not found]
```