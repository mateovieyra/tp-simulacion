
""" def s1(t):
    print(beta)
    print(h)
    print(s0)
    print(i0)
    return (-1 * beta) * q(t, s0, h, s1) * q(t, i0, h, i1)

def i1(t):
    return beta * q(t, s0, h, s1) * q(t, i0, h, i1) - v + q(t, i0, h, i1)

def r1(t):
    return v * q(t, i0, h, i1) """

""" def r(t, h, beta, v, s0, i0, r0):
    if t <= 0:
        return r0
    else:
        return r(t-h, h, beta, v, s0, i0, r0) + h * v * i(t-h, h, beta, v, s0, i0, r0)

def i(t, h, beta, v, s0, i0, r0):
    if t <= 0:
        return i0
    else:
        return i(t-h, h, beta, v, s0, i0, r0) + h * beta * s(t-h, h, beta, v, s0, i0, r0) - v * i(t-h, h, beta, v, s0, i0, r0)
        

def s(t, h, beta, v, s0, i0, r0):
    if t <= 0:
        return s0
    else:
        return s(t-h, h, beta, v, s0, i0, r0) + h * (-1 * beta) * s(t-h, h, beta, v, s0, i0, r0) * i(t-h, h, beta, v, s0, i0, r0) 
  """

# Diccionario para almacenar los resultados memoizados
memo_retired = {}

def retired_deritative(t, h, beta, v, s0, i0, r0):
    if t <= 0:
        return r0
    elif t in memo_retired:  # Comprobar si el resultado ya está memoizado
        return memo_retired[t]
    else:
        result = retired_deritative(t-h, h, beta, v, s0, i0, r0) + h * v * infected_deritative(t-h, h, beta, v, s0, i0, r0)
        memo_retired[t] = result  # Almacenar el resultado memoizado
        return result

memo_infected = {}

def infected_deritative(t, h, beta, v, s0, i0, r0):
    if t <= 0:
        return i0
    elif t in memo_infected:
        return memo_infected[t]
    else:
        result = infected_deritative(t-h, h, beta, v, s0, i0, r0) + h * beta * suceptible_deritative(t-h, h, beta, v, s0, i0, r0) - v * infected_deritative(t-h, h, beta, v, s0, i0, r0)
        memo_infected[t] = result
        return result

memo_suceptible = {}

def suceptible_deritative(t, h, beta, v, s0, i0, r0):
    if t <= 0:
        return s0
    elif t in memo_suceptible:
        return memo_suceptible[t]
    else:
        result = suceptible_deritative(t-h, h, beta, v, s0, i0, r0) + h * (-beta) * suceptible_deritative(t-h, h, beta, v, s0, i0, r0) * infected_deritative(t-h, h, beta, v, s0, i0, r0)
        memo_suceptible[t] = result
        return result

def y(t, h):
    if t == 0:
        return 1
    else:
        return y(t - h, h) + h * (y(t-h, h) * -1)


# Generic euler function
def q(t:float, base_case:float, h:float, derived_function):
    if t <= 0:
        return base_case
    else:
        return q(t-h, base_case, h, derived_function) + h * derived_function(t-h)
