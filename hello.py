from mpi4py import MPI

def hello():
    """
    Basic hello world with rank+size.
    """
    rank = MPI.COMM_WORLD.Get_rank()
    size = MPI.COMM_WORLD.Get_size()

    print('Hello World! from rank {}/{}'.format(rank, size))


if __name__ == '__main__':
    hello()
