def sift_down(A, size, i):
    """
    Restore min-heap property starting at index i.
    Time: O(log size)
    Space: O(1)
    """
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < size and A[left] < A[smallest]:
            smallest = left
        if right < size and A[right] < A[smallest]:
            smallest = right

        if smallest == i:
            break

        # swap
        A[i], A[smallest] = A[smallest], A[i]
        i = smallest


def build_min_heap(A):
    """
    Convert array A into a min-heap in place.
    Time: O(n)
    Space: O(1)
    """
    size = len(A)
    # start from last internal node
    for i in range(size // 2 - 1, -1, -1):
        sift_down(A, size, i)


def magic(T1, T2):
    """
    Merge two min-heaps T1 and T2 into a new min-heap T3.
    Time: O(n + m)
    Aux space: O(n + m)
    """
    # Step 1: copy values
    T3 = []
    for x in T1:
        T3.append(x)
    for x in T2:
        T3.append(x)

    # Step 2: build min-heap
    build_min_heap(T3)

    return T3