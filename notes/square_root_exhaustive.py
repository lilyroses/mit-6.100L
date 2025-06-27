# epsilon_exhaustive_search.py
x = float(input("x: "))

def square_root(x):
    epsilon = 0.01
    step = epsilon**3
    guesses = 0
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
        ans += step
        guesses += 1
    print(f"Guesses: {guesses}")
    if abs(ans**2 - x) >= epsilon:
        print(f"Failed on square root of {x}")
    else:
        print(f"{ans} is close to square root of {x}")


square_root(x)