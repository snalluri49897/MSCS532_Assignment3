import random
import time
from typing import List
import sys

sys.setrecursionlimit(30000)

# Randomized Quicksort
def randomized_quicksort(arr: List[int]) -> List[int]:
    arr = arr.copy()
    _randomized_quicksort(arr, 0, len(arr) - 1)
    return arr


def _randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        _randomized_quicksort(arr, low, pivot_index - 1)
        _randomized_quicksort(arr, pivot_index + 1, high)


def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)


# Deterministic Quicksort
# First element as pivot
def deterministic_quicksort(arr: List[int]) -> List[int]:
    arr = arr.copy()
    _deterministic_quicksort(arr, 0, len(arr) - 1)
    return arr


def _deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = deterministic_partition(arr, low, high)
        _deterministic_quicksort(arr, low, pivot_index - 1)
        _deterministic_quicksort(arr, pivot_index + 1, high)


def deterministic_partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


# Shared Partition Function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1



# Benchmarking
def benchmark():
    sizes = [1000, 5000, 10000]

    print("=" * 80)
    print("Randomized Quicksort vs Deterministic Quicksort")
    print("=" * 80)

    for n in sizes:
        print(f"\nArray Size = {n}")
        print("-" * 80)

        datasets = {
            "Random": [random.randint(1, 100000) for _ in range(n)],
            "Sorted": list(range(n)),
            "Reverse Sorted": list(range(n, 0, -1)),
            "Repeated Elements": [random.randint(1, 10) for _ in range(n)]
        }

        for name, data in datasets.items():

            # Randomized Quicksort Timing
            start = time.perf_counter()
            randomized_quicksort(data)
            randomized_time = time.perf_counter() - start

            # Deterministic Quicksort Timing
            try:
                start = time.perf_counter()
                deterministic_quicksort(data)
                deterministic_time = time.perf_counter() - start

                det_time_str = f"{deterministic_time:.6f}s"

            except RecursionError:
                det_time_str = "RecursionError"

            print(
                f"{name:20s} | "
                f"Randomized: {randomized_time:.6f}s | "
                f"Deterministic: {det_time_str}"
            )


if __name__ == "__main__":
    benchmark()