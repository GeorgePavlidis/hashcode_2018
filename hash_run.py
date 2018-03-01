
def read_data(infile):

    with open(infile, 'r') as fin:

        X1, X2, X3, X4 = [int(num) for num in fin.readline().split()]

        return X1, X2, X3, X4
