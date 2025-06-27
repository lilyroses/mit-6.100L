## 6.100A PSet 1: Part C
## Name: Lily Stracke
## Time Spent: start: 4:22pm
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
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
amount_saved = initial_deposit * (1 + (r/12))
steps = 0


print(f"Best savings rate: {
