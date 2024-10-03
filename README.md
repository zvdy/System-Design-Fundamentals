# System Design

This repository contains detailed explanations and Python code examples for various system design topics. Each topic is organized into its own folder with a `README.md` file and relevant code examples to help you understand the concepts better.

## Index
1. [Performing A Systems Design Interview](#performing-a-systems-design-interview)
2. [Database Fundamentals](#database-fundamentals)
3. [Data Serialization Frameworks](#data-serialization-frameworks)
4. [Replication](#replication)
5. [Sharding](#sharding)
6. [Batch Processing](#batch-processing)
7. [Stream Processing](#stream-processing)
8. [Other Types Of Storage](#other-types-of-storage)
9. [Caching](#caching)
10. [Load Balancing](#load-balancing)
11. [Systems Design Interview Patterns](#systems-design-interview-patterns)

### [Performing A Systems Design Interview](performing_system_design_interview/README.md)
- **Topic:** Performing A Systems Design Interview
- **Summary:** 
  - **Key Steps:**
    - **Clarify Requirements:** Understand the problem statement, ask clarifying questions, and gather all necessary requirements.
    - **Define Scope:** Determine the scope of the system to be designed, including any constraints and assumptions.
    - **High-Level Architecture:** Outline the high-level architecture, including major components and their interactions.
    - **Detailed Design:** Dive into the details of each component, discussing data flow, algorithms, and data structures.
    - **Trade-offs and Justifications:** Discuss trade-offs for different design choices and justify your decisions.
    - **Scalability and Reliability:** Consider scalability, reliability, and fault tolerance in your design.
    - **Communication:** Clearly communicate your thought process and design decisions throughout the interview.

### [Database Fundamentals](database_fundamentals/README.md)
- **Topic:** Database Fundamentals
- **Summary:** 
  - **Relational Databases (RDBMS):**
    - **Characteristics:** Structured data, ACID properties (Atomicity, Consistency, Isolation, Durability).
    - **Examples:** MySQL, PostgreSQL, Oracle.
    - **Use Cases:** Transactional systems, applications requiring complex queries and joins.
  - **Non-Relational Databases (NoSQL):**
    - **Types:** Document stores (e.g., MongoDB), key-value stores (e.g., Redis), column-family stores (e.g., Cassandra), graph databases (e.g., Neo4j).
    - **Characteristics:** Schema-less, horizontal scalability, eventual consistency.
    - **Use Cases:** Big data applications, real-time analytics, flexible schema requirements.
  - **CAP Theorem:** Consistency, Availability, Partition Tolerance - trade-offs in distributed databases.
  - **ACID vs. BASE:** ACID for strong consistency, BASE (Basically Available, Soft state, Eventual consistency) for high availability.

### [Data Serialization Frameworks](data_serialization_frameworks/README.md)
- **Topic:** Data Serialization Frameworks
- **Summary:** 
  - **Definition:** Process of converting data structures or object states into a format that can be stored or transmitted and reconstructed later.
  - **Common Formats:**
    - **JSON:** Human-readable, widely used in web APIs, less efficient in terms of size and speed.
    - **XML:** Human-readable, supports complex data structures, verbose and slower.
    - **Protocol Buffers:** Developed by Google, efficient binary format, requires schema definition.
    - **Avro:** Developed by Apache, supports dynamic typing and schema evolution, efficient binary format.
    - **Thrift:** Developed by Facebook, supports multiple languages, efficient binary format.
  - **Use Cases:** Data exchange between services, storage, configuration files.
  - **Performance Considerations:** Serialization/deserialization speed, data size, interoperability.

### [Replication](replication/README.md)
- **Topic:** Replication
- **Summary:** 
  - **Definition:** Process of copying and maintaining database objects in multiple database servers.
  - **Types:**
    - **Synchronous Replication:** Ensures data consistency across replicas, higher latency.
    - **Asynchronous Replication:** Faster, eventual consistency, risk of data loss in case of failure.
  - **Models:**
    - **Master-Slave Replication:** One master node handles writes, multiple slave nodes handle reads.
    - **Master-Master Replication:** Multiple master nodes handle both reads and writes, more complex conflict resolution.
  - **Challenges:** Data consistency, conflict resolution, network latency.
  - **Use Cases:** High availability, disaster recovery, load balancing.

### [Sharding](sharding/README.md)
- **Topic:** Sharding
- **Summary:** 
  - **Definition:** Technique to distribute data across multiple machines to improve scalability.
  - **Types:**
    - **Horizontal Sharding:** Distributes rows of a table across multiple shards.
    - **Vertical Sharding:** Distributes columns of a table across multiple shards.
  - **Sharding Strategies:**
    - **Range-Based Sharding:** Shards data based on a range of values.
    - **Hash-Based Sharding:** Uses a hash function to distribute data evenly.
    - **Directory-Based Sharding:** Uses a lookup table to determine the shard for each data item.
  - **Challenges:** Rebalancing shards, cross-shard queries, maintaining consistency.
  - **Use Cases:** Large-scale applications, distributed databases.

### [Batch Processing](batch_processing/README.md)
- **Topic:** Batch Processing
- **Summary:** 
  - **Definition:** Processing large volumes of data in batches at scheduled intervals.
  - **Characteristics:** High throughput, latency-tolerant, suitable for ETL jobs.
  - **Frameworks:** Hadoop, Apache Spark.
  - **Use Cases:** Data warehousing, data migration, periodic reporting.
  - **Performance Considerations:** Resource allocation, job scheduling, fault tolerance.

### [Stream Processing](stream_processing/README.md)
- **Topic:** Stream Processing
- **Summary:** 
  - **Definition:** Processing data in real-time as it arrives.
  - **Characteristics:** Low latency, continuous processing, suitable for real-time analytics.
  - **Frameworks:** Apache Kafka, Apache Flink, Apache Storm.
  - **Use Cases:** Real-time monitoring, event detection, live dashboards.
  - **Challenges:** Handling high-velocity data, ensuring data consistency, fault tolerance.

### [Other Types Of Storage](other_types_of_storage/README.md)
- **Topic:** Other Types Of Storage
- **Summary:** 
  - **Object Storage:** 
    - **Examples:** Amazon S3, Google Cloud Storage.
    - **Characteristics:** Stores data as objects, scalable, suitable for unstructured data.
    - **Use Cases:** Backup and archival, media storage, big data analytics.
  - **Block Storage:**
    - **Examples:** Amazon EBS, Google Persistent Disk.
    - **Characteristics:** Provides raw storage blocks, high performance, suitable for databases.
    - **Use Cases:** Databases, virtual machine storage, high-performance applications.
  - **File Storage:**
    - **Examples:** NFS, SMB.
    - **Characteristics:** Stores data as files, hierarchical structure, suitable for shared access.
    - **Use Cases:** File sharing, content management systems, home directories.

### [Caching](caching/README.md)
- **Topic:** Caching
- **Summary:** 
  - **Definition:** Temporary storage of data for quick access.
  - **Types:**
    - **In-Memory Caches:** Redis, Memcached.
    - **Distributed Caches:** Hazelcast, Apache Ignite.
  - **Cache Eviction Policies:** LRU (Least Recently Used), LFU (Least Frequently Used), FIFO (First In First Out).
  - **Strategies:** Cache-aside, write-through, write-back.
  - **Use Cases:** Improving read performance, reducing database load, speeding up web applications.

### [Load Balancing](load_balancing/README.md)
- **Topic:** Load Balancing
- **Summary:** 
  - **Definition:** Distributing incoming network traffic across multiple servers.
  - **Types:**
    - **Hardware Load Balancers:** Dedicated devices, high performance, expensive.
    - **Software Load Balancers:** NGINX, HAProxy, flexible, cost-effective.
    - **Layer 4 vs. Layer 7 Load Balancers:** Layer 4 operates at the transport layer, Layer 7 operates at the application layer.
  - **Algorithms:** Round-robin, least connections, IP hash.
  - **Challenges:** Session persistence, SSL termination, handling failures.
  - **Use Cases:** Ensuring high availability, improving performance, scaling applications.

### [Systems Design Interview Patterns](systems_design_interview_patterns/README.md)
- **Topic:** Systems Design Interview Patterns
- **Summary:** 
  - **Common Patterns:**
    - **Microservices:** Decomposing applications into small, independent services.
    - **Event-Driven Architecture:** Using events to trigger and communicate between services.
    - **CQRS (Command Query Responsibility Segregation):** Separating read and write operations.
  - **Scalability:** Designing systems to handle increased load.
  - **Reliability:** Ensuring system availability and fault tolerance.
  - **Maintainability:** Designing systems that are easy to maintain and extend.
  - **Failure Handling:** Techniques for detecting and recovering from failures.
  - **Communication:** Effectively communicating design choices and trade-offs during the interview.