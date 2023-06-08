import argparse

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", help="Time in days of the simulation.")
    parser.add_argument("-d", "--delta", help="H parameter. Step measure in hours.")
    parser.add_argument("-b", "--beta", help="Beta. Per-capita infection rate.")
    parser.add_argument("-v", "--v", help="V parameter. Retirement rate")
    parser.add_argument("-s", "--s0", help="Initial value of Susceptible People.")
    parser.add_argument("-i", "--i0", help="Initial value of Infected People.")
    parser.add_argument("-r", "--r0", help="Initial value of Retired People.")
    args = parser.parse_args()
    return args