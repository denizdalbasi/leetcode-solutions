# 88. Merge Sorted Array

| Language | Approach | Runtime | Memory |
| :--- | :--- | :--- | :--- |
| Python | Three-Pointer Backward Insertion | 0 ms | 19.14 MB |

### Approach Analysis
The constraint requires merging `nums2` into `nums1` in-place. A forward approach would require shifting elements and ruining the linear time complexity. To avoid this, I used three pointers (`p1` for `nums1` data, `p2` for `nums2`, and `p` for the write destination) to fill `nums1` **backwards** starting from the empty trailing zeros. By comparing the largest remaining elements at `p1` and `p2`, the absolute largest element is safely written to `p` without overwriting unvisited data in `nums1`. If `nums2` still has elements left after `nums1` is exhausted, they are copied directly over.