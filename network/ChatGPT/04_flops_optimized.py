#optimize solution based on FLOPS

# Optimizing for FLOPS (floating-point operations per second) typically involves reducing the number of operations or finding more efficient ways to perform computations. In this context, the main computation happens when updating distances and using a priority queue. Since Dijkstra's algorithm complexity depends on the number of edges and nodes, there isn't a straightforward way to optimize for FLOPS directly. However, we can provide some general guidelines to minimize computational overhead:

# 1. **Priority Queue Implementation:** Choose a priority queue implementation that provides efficient operations. Python's built-in `heapq` module uses a binary heap and is already quite efficient. Using a more advanced data structure, like a Fibonacci heap, can potentially reduce the number of operations further.

# 2. **Avoid Unnecessary Operations:** Within the priority queue loop, only update distances when you have found a shorter path. This avoids unnecessary comparisons and updates. Additionally, skip nodes that are already processed and don't need to be revisited.

# 3. **Use Bitwise Operations:** In some cases, bitwise operations can be used to optimize certain arithmetic operations. However, this might not directly apply to this problem as it's not heavily reliant on arithmetic computations.

# 4. **Parallelism:** If you have a multi-core CPU, you might consider parallelizing some parts of the algorithm. For instance, the exploration of different paths from a node can be done concurrently.

# 5. **Memory Access Patterns:** Optimize memory access patterns to make use of CPU cache efficiently. This could involve arranging data structures in a cache-friendly way.

# Remember that optimizing for FLOPS in this context might not result in drastic improvements since Dijkstra's algorithm is inherently based on graph traversal and priority queue operations. It's important to strike a balance between optimizing for performance and maintaining code readability and maintainability.
