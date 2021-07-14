from typing import List

MAX = 10000


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    elif num > 1:
        for j in range(2, num // 2):
            if (num % j) == 0:
                return False
    return True


def is_growing(num: int) -> bool:
    num_arr: List[int] = [int(el) for el in list(str(num))]
    if len(num_arr) > 1:
        for j in range(len(num_arr) - 1):
            if num_arr[j] >= num_arr[j + 1]:
                return False
    return True


result_arr: List[int] = []
for number in range(MAX + 1):
    if is_prime(number):
        if is_growing(number):
            result_arr.append(number)

print(f"Result: {result_arr}")  # Prime growing numbers
print(f"There are {len(result_arr)} prime growing numbers between 1 and {MAX}")
