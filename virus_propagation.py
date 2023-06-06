from parser import parse_input

def hours_to_days(t):
    return t/24

 
""" def fun():
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib import pyplot as plt """


t = 0
beta = 0
v = 0
s0 = 0
i0 = 0
r0 = 0
t = 0
h = 0
if __name__ == "__main__":
    from derived_functions import q, s1

    args = parse_input()

    t = args.time
    beta = args.beta
    v = args.v
    s0 = args.s0
    i0 = args.i0
    r0 = args.r0

    i = 0
    h = 0.5
    print(q(2, 1, h, s1))
    while i <= 3.0:
        i += 0.5
