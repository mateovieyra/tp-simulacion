
# Dictionary for allocating all the results of the retired people function.
memo_retired = {}

# This function represents the amount of retired people.
# t: time in days
# h: step measure in hours
# beta: per-capita infection rate
# v: retirement rate
# s0: initial value of susceptible people
# i0: initial value of infected people
# r0: initial value of retired people
def retired_function(t, h, beta, v, s0, i0, r0):
    if t <= 0:
        return r0
    elif t in memo_retired:  # For making the function more efficient, we use memoization.
        return memo_retired[t]
    else:
        result = retired_function(t-h, h, beta, v, s0, i0, r0) + h * (v * infected_function(t-h, h, beta, v, s0, i0, r0))
        memo_retired[t] = result 
        return result

# Dictionary for allocating all the results of the infected people function.
memo_infected = {}

# This function represents the amount of retired people.
def infected_function(t, h, beta, v, s0, i0, r0):
    if t <= 0:
        return i0
    elif t in memo_infected:
        return memo_infected[t]
    else:
        result = infected_function(t-h, h, beta, v, s0, i0, r0) + h * (beta * suceptible_function(t-h, h, beta, v, s0, i0, r0) * infected_function(t-h, h, beta, v, s0, i0, r0) - v * infected_function(t-h, h, beta, v, s0, i0, r0))
        memo_infected[t] = result
        return result

# Dictionary for allocating all the results of the susceptible people function.
memo_suceptible = {}

# This function represents the amount of retired people.
def suceptible_function(t, h, beta, v, s0, i0, r0):
    if t <= 0:
        return s0
    elif t in memo_suceptible:
        return memo_suceptible[t]
    else:
        result = suceptible_function(t-h, h, beta, v, s0, i0, r0) + h * ((-beta) * suceptible_function(t-h, h, beta, v, s0, i0, r0) * infected_function(t-h, h, beta, v, s0, i0, r0))
        memo_suceptible[t] = result
        return result