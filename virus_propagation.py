import matplotlib
import matplotlib.pyplot as plt

from functions import suceptible_function, retired_function, infected_function
from parser_1 import parse_input

# This function converts the time in days to hours.
def hours_to_days(t):
    return t/24

# This function generates the plot, with the input parameters.
def make_plot(time, h, beta, v, s0, i0, r0):
    matplotlib.use('TkAgg')
    x = []
    j = 0
    while (j < time):
        x.append(j)
        j+=h

    y0 = [suceptible_function(j, h, beta, v, s0, i0, r0) for j in x]
    y1 = [infected_function(j, h, beta, v, s0, i0, r0) for j in x]
    y2 = [retired_function(j, h, beta, v, s0, i0, r0) for j in x]
   
    plt.plot(x, y0, linewidth=2.0, color='blue', label='Susceptible People')
    plt.plot(x, y1, linewidth=2.0, color='red', label='Infected People')
    plt.plot(x, y2, linewidth=2.0, color='green', label='Retired People')
    plt.title('Virus Propagation')
    plt.xlabel("Time in days")
    plt.ylabel("People")
    plt.legend()
    plt.show()

if __name__ == "__main__":

    args = parse_input()

    t = float(args.time)
    h = float(args.delta)
    beta = float(args.beta)
    v = float(args.v)
    s0 = float(args.s0)
    i0 = float(args.i0)
    r0 = float(args.r0)

    make_plot(t, hours_to_days(h), beta, v, s0, i0, r0)
