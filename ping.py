from mpi4py import MPI

def ping():
    """
    Two processus exchange pings.
    """
    rank = MPI.COMM_WORLD.Get_rank()
    if rank >= 2:
        return # Only taking the first two processus in account here.

    other_rank = (rank + 1) % 2

    MPI.COMM_WORLD.send('ping from {}'.format(str(rank)), dest=other_rank)
    msg = MPI.COMM_WORLD.recv(source=other_rank)

    print('My ID: {}\tMSG: {}'.format(str(rank), msg))

if __name__ == '__main__':
    assert MPI.COMM_WORLD.Get_size() >= 2, 'This test needs two processus'
    ping()
