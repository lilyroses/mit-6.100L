# bisect_search.py
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


nums = list(range(1, 10_001))
val = int(input("Enter a number between 0 and 10,000: "))

if val < nums[0] or val > nums[-1]:
    print(f"Error: {val} out of range")
else:
    print(bisect_search(nums, val))