def find_r(initial_deposit):
    cost_of_dream_home = 800_000
    portion_down_payment = cost_of_dream_home * 0.25

    steps = 0

    high = 1_000_000_000_000
    low = 0

    while True:
        steps += 1

        mid = (low+high) // 2       
        r = mid / 1_000_000_000_000

        amount_saved = initial_deposit
        for i in range(36):
            amount_saved += round((amount_saved * (r/12)), 2)

        # print(f"\nlow={low}, high={high}, mid={mid}, r={r}, amount_saved={amount_saved}")

        if amount_saved > (portion_down_payment+100):
            print(f"r is TOO HIGH")
            high = mid-1

        elif amount_saved < (portion_down_payment-100):
            print(f"r is TOO LOW")
            low = mid+1
        else:
            print(f"Best savings rate: {r}")
            print(f"Steps in bisection search: {steps}")
            return


initial_deposit = float(input("Enter the initial deposit: "))

find_r(initial_deposit)