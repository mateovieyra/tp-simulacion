import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from derived_functions import q, suceptible_deritative, retired_deritative, infected_deritative
from parser_1 import parse_input

def hours_to_days(t):
    return t*24

def make_plot(time, h, beta, v, s0, i0, r0):
    matplotlib.use('TkAgg')
    x = []
    j = 0
    while (j < time):
        x.append(j)
        j+=h

    y0 = [suceptible_deritative(j, h, beta, v, s0, i0, r0) for j in x]
    y1 = [infected_deritative(j, h, beta, v, s0, i0, r0) for j in x]
    y2 = [retired_deritative(j, h, beta, v, s0, i0, r0) for j in x]
   
    plt.plot(x, y0, linewidth=2.0, color='blue', label='Susceptible People')
    plt.plot(x, y1, linewidth=2.0, color='red', label='Infected People')
    plt.plot(x, y2, linewidth=2.0, color='green', label='Retired People')
    plt.title('Virus Propagation')
    plt.legend()
    plt.show()

    """ ax0.plot(x, y0, linewidth=2.0)
    ax1.plot(x, y1, linewidth=2.0)
    ax2.plot(x, y2, linewidth=2.0)
    
    ax0.legend()
    ax0.set_xlabel('Time (hours)')
    ax0.set_ylabel('Susceptible People')
    
    ax1.legend()
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('Infected People')
    
    ax2.legend()
    ax2.set_xlabel('Time (hours)')
    ax2.set_ylabel('Retired People')


    ax0.set_xticks(np.arange(0,700, 24))
    ax0.set_yticks(np.arange(0,1000, 50))
    ax1.set_xticks(np.arange(0,700, 24))
    ax1.set_yticks(np.arange(0,1000, 50))
    ax2.set_xticks(np.arange(0,700, 24))
    ax2.set_yticks(np.arange(0,1000, 50))
 """

if __name__ == "__main__":

    args = parse_input()

    t = float(args.time)
    h = float(args.delta)
    beta = float(args.beta)
    v = float(args.v)
    s0 = float(args.s0)
    i0 = float(args.i0)
    r0 = float(args.r0)

    print(suceptible_deritative(t, h, beta, v, s0, i0, r0))
    print(infected_deritative(t, h, beta, v, s0, i0, r0))
    print(retired_deritative(t, h, beta, v, s0, i0, r0))


    make_plot(hours_to_days(t), h, beta, v, s0, i0, r0)
