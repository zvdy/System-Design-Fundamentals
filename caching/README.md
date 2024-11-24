### Caching

**Topic:** Caching

**Summary:**

- **Definition:** Temporary storage of data for quick access.
  - Caching involves storing copies of data in a temporary storage location (cache) so that future requests for that data can be served faster.

- **Types:**
  - **In-Memory Caches:** These caches store data in the system's RAM, providing very fast access times. Examples include:
    - **Redis:** An open-source, in-memory data structure store used as a database, cache, and message broker.
    - **Memcached:** A distributed memory caching system used to speed up dynamic web applications by alleviating database load.
  - **Distributed Caches:** These caches are spread across multiple servers, allowing for larger datasets and improved fault tolerance. Examples include:
    - **Hazelcast:** An in-memory data grid that provides distributed caching and computing.
    - **Apache Ignite:** A distributed database, caching, and processing platform designed for high-performance computing.

- **Cache Eviction Policies:** These policies determine how data is removed from the cache when it becomes full. Common policies include:
  - **LRU (Least Recently Used):** Removes the least recently accessed items first.
  - **LFU (Least Frequently Used):** Removes the least frequently accessed items first.
  - **FIFO (First In First Out):** Removes the oldest items first.

- **Strategies:**
  - **Cache-aside:** The application is responsible for loading data into the cache as needed. If the data is not in the cache (cache miss), it is fetched from the original data source and then stored in the cache.
  - **Write-through:** Data is written to both the cache and the original data source simultaneously, ensuring consistency.
  - **Write-back:** Data is initially written to the cache only and later persisted to the original data source, which can improve write performance but requires careful handling to ensure data consistency.

- **Use Cases:** Caching is used in various scenarios to improve performance and efficiency, such as:
  - **Improving read performance:** By storing frequently accessed data in the cache, read operations can be performed much faster.
  - **Reducing database load:** Caching can offload read requests from the database, reducing its load and improving overall system performance.
  - **Speeding up web applications:** Caching can store web pages, API responses, and other data to reduce latency and improve user experience.