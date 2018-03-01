import argparse


def read_data(infile):

    with open(infile, 'r') as fin:

        R, C, F, N, B, T = [int(num) for num in fin.readline().split()]

        rides = []
        for _ in range(N):
            ride = [int(num) for num in fin.readline().split()]
            rides.append(ride)

        return R, C, F, N, B, T, rides


def calc_distance(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    d = abs(x2 - x1) + abs(y2 - y1)
    return d



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help='input file')
    infile = parser.parse_args().input
    data = read_data(infile)
    print(data)

