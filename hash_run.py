import argparse


def read_data(infile):

    with open(infile, 'r') as fin:

        rows, columns, vehicles, num_rides, bonus, steps = [int(num) for num in fin.readline().split()]

        rides = []
        for _ in range(num_rides):
            ride = [int(num) for num in fin.readline().split()]
            rides.append(ride)

        return rows, columns, vehicles, num_rides, bonus, steps, rides


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

