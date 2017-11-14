from mpi4py import MPI


def get_left(rank):
    return 2 * rank + 1


def get_right(rank):
    return 2 * rank + 2


def get_parent(rank):
    return (rank - 1) // 2


def forward(msg, rank, size):
    left = get_left(rank)
    right = get_right(rank)

    if left < size:
        MPI.COMM_WORLD.send(msg, dest=left)
    if right < size:
        MPI.COMM_WORLD.send(msg, dest=right)


def tree():
    """
    Send a message to all processus throught a tree topology.
    The root node is 0, left child is 2*N+1, right child is 2*N+2, and parent
    is (N-1)/2.

    Example:
    [ 0 1 2 3 4 5 6 ]
            0
        1       2
      3   4   5   6
    """
    rank = MPI.COMM_WORLD.Get_rank()
    size = MPI.COMM_WORLD.Get_size()



    if rank == 0: # Root node
        print('Ping from root 0')
        forward('ping', rank, size)
    else:
        msg = MPI.COMM_WORLD.recv(source=get_parent(rank))
        print('ID: {}\tMSG: {}'.format(rank, msg))
        forward(msg, rank, size)


if __name__ == '__main__':
    assert MPI.COMM_WORLD.Get_size() > 1, 'Provide at least two processus'
    tree()
