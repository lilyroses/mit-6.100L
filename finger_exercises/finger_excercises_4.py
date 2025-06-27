# finger_excercises_4.py
N = 8

ans = 0
while ans**3 < abs(N):
    ans = ans+1
if ans**3 != abs(N):
    print(f"{N} is not a perfect cube")
else:
    if N < 0:
        ans = -ans
    print(f"Cube root of N is {ans}")
