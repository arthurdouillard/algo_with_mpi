from mpi4py import MPI

def ring():
    """
    Send a message to all processus throught a ring topology.
    The first to send the message is 0.
    """
    rank = MPI.COMM_WORLD.Get_rank()
    size = MPI.COMM_WORLD.Get_size()

    if rank == 0: # Send initial message
        MPI.COMM_WORLD.send('ping', dest=1)

    msg = MPI.COMM_WORLD.recv(source=(rank - 1) % size)
    print('ID: {}, just received: {}'.format(rank, msg))
    MPI.COMM_WORLD.send(msg, dest=(rank + 1) % size)


if __name__ == '__main__':
    assert MPI.COMM_WORLD.Get_size() > 1, 'Provide at least two processus.'
    ring()
