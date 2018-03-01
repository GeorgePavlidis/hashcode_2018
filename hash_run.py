import argparse

def read_data(infile):

    with open(infile, 'r') as fin:

        R, C, F, N, B, T = [int(num) for num in fin.readline().split()]

        rides = []
        for _ in range(N):
            ride = [int(num) for num in fin.readline().split()]
            rides.append(ride)


        return R, C, F, N, B, T, rides


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help='input file')
    infile = parser.parse_args().input
    data = read_data(infile)
    print(data)

