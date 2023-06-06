import argparse

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", help="Time in days")
    parser.add_argument("-d", "--delta", help="H parameter, or delta")
    parser.add_argument("-b", "--beta", help="Beta parameter")
    parser.add_argument("-v", "--v", help="V parameter")
    parser.add_argument("-s", "--s0", help="Susceptible People")
    parser.add_argument("-i", "--i0", help="Infected People")
    parser.add_argument("-r", "--r0", help="Retired People")
    args = parser.parse_args()
    return args