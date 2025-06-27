# square_root_bisect_search.py
from math import ceil, log2

nums = list(range(1, 100_000))
val = 42


def log2(x):
    return ceil(log2(x))

def bisect_search(nums, val):
    steps = 0
    high = len(nums)
    low = 0

    while True:
        steps += 1
        mid = (high+low) // 2
        guess = nums[mid]
        print(f"high={high}, low={low}, mid={mid}, guess={guess}, steps={steps}")

        if guess == val:
            return steps

        if guess > val:
            high = mid-1
        
        elif guess < val:
            low = mid+1


print(bisect_search(nums, val))