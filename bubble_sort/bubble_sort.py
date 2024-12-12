def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    import time
    import random

    # Generate random data
    data = [random.randint(0, 1000) for _ in range(1000)]

    start_time = time.time()
    bubble_sort(data)
    print(f"Sorted in: {time.time() - start_time:.5f} seconds")
