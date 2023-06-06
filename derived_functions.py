from virus_propagation import beta, v, h, s0, i0

def s1(t):
    print(beta)
    print(h)
    print(s0)
    print(i0)
    return (-1 * beta) * q(t, s0, h, s1) * q(t, i0, h, i1)

def i1(t):
    return beta * q(t, s0, h, s1) * q(t, i0, h, i1) - v + q(t, i0, h, i1)

def r1(t):
    return v * q(t, i0, h, i1)

""" def r(t, h, beta, v, s0, i0, r0):
    if r0 == 0:
        return r0
    else:
        return r(t-h, h, beta, v s0, i0, r0) + h * v * i(t-h, h, beta, v, s0, i0, r0)

def i(t, h, beta, v, s0, i0, r0):
    if i0 == 0:
        return i0
    else:
        return i(t-h, h, beta, v s0, i0, r0) + h * beta * s(t-h, h, beta, v, s0, i0, r0) - v * i(t-h, h, beta, v s0, i0, r0)
        

def s(t, h, beta, v, s0, i0, r0):
    if s0 == 0:
        return s0
    else:
        return s(t-h, h, beta, v, s0, i0, r0) + h * (-1 * beta) * s(t-h, h, beta, v, s0, i0, r0) * i(t-h, h, beta, v s0, i0, r0) """
        

def y(t, h):
    if t == 0:
        return 1
    else:
        return y(t - h, h) + h * (y(t-h, h) * -1)


# Generic euler function
def q(t:float, base_case:float, h:float, derived_function):
    if t == 0:
        return base_case
    else:
        return q(t-h, base_case, h, derived_function) + h * derived_function(t-h)
