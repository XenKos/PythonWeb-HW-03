import time
from multiprocessing import Pool, cpu_count

def factorize(numbers):
    result = []
    for num in numbers:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        result.append(factors)
    return result

def factorize_single(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize_single, numbers)

if __name__ == "__main__":
    
    numbers = [1000000, 1000001, 1000002, 1000003, 1000004]

    start_time_sync = time.time()
    factorize_result_sync = factorize(numbers)
    end_time_sync = time.time()
    execution_time_sync = end_time_sync - start_time_sync

    print("Execution time (synchronous):", execution_time_sync)

    
    start_time_parallel = time.time()
    factorize_result_parallel = factorize_parallel(numbers)
    end_time_parallel = time.time()
    execution_time_parallel = end_time_parallel - start_time_parallel

    print("Execution time (parallel):", execution_time_parallel)

    print("Speedup factor:", execution_time_sync / execution_time_parallel)