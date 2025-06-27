## 6.100A PSet 1: Part C
## Name: Lily Stracke
## Time Spent: ~ 5hrs
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter your initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800_000
portion_down_payment = cost_of_dream_home * 0.25

##################################################################################################
## Determine the lowest rate of return needed to get the down payme nt for your dream home below ##
##################################################################################################
if initial_deposit >= (portion_down_payment-100):
    r = 0.0
    print(f"Best savings rate: {r}")        
    print(f"Steps in bisection search: {steps}")

else:
    steps = 0

    high = 1_000_000_000_000
    low = 0

    while True:

        steps += 1

        mid = (low+high) // 2       
        
        if mid == low or mid == high:
            r = None
            print(f"Best savings rate: {r}")
            print(f"Steps in bisection search: {steps}")
            break

        r = mid / 1_000_000_000_000
        
        amount_saved = initial_deposit
        for i in range(36):
            amount_saved += round((amount_saved * (r/12)), 2)
        
        if amount_saved > (portion_down_payment+100):
            print(f"r is TOO HIGH")
            high = mid-1

        elif amount_saved < (portion_down_payment-100):
            print(f"r is TOO LOW")
            low = mid+1
        else:
            print(f"Best savings rate: {r}")
            print(f"Steps in bisection search: {steps}")
            break
