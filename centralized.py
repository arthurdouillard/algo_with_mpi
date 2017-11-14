from mpi4py import MPI

def centralized():
    """
    Each processus send a message to its next, all messages must passed throught
    the `master`, aka processus 0.
    """
    rank = MPI.COMM_WORLD.Get_rank()
    size = MPI.COMM_WORLD.Get_size()
    master = 0

    MPI.COMM_WORLD.send('ping from {}'.format(str(rank)), dest=0)
    if rank == 0: # I am currently the master.
        for i in range(size):
            msg = MPI.COMM_WORLD.recv(source=i)
            MPI.COMM_WORLD.send(msg, dest=(i + 1) % size)

    msg = MPI.COMM_WORLD.recv(source=0)
    print('ID: {}\tMSG: {}'.format(rank, msg))


if __name__ == '__main__':
    assert MPI.COMM_WORLD.Get_size() > 1, 'Provide at least two processus.'
    centralized()
