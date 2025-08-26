from multiprocessing import Pool
import time

def square(n):
    return n * n

if _name_ == "_main_":
    numbers = list(range(1_000_000))  # Large list
    start = time.time()

    with Pool() as pool:
        results = pool.map(square, numbers)

    end = time.time()
    print(f"First 10 results: {results[:10]}")
    print(f"Time taken: {end - start:.2f} seconds")