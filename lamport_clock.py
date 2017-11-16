import time
import random

from mpi4py import MPI


class LamportClock:
    def __init__(self, rank, size, clock=0, lifespan=None):
        self.lifespan = lifespan
        self.rank = rank
        self.size = size
        self.universe = list(range(0, rank)) + list(range(rank+1, size))
        self.clock = clock


    def recv(self, verbose=True):
        """
        Message format:
            msg1\\nmsg2\\n...\\ntimestamp
        """
        msg = MPI.COMM_WORLD.recv(source=MPI.ANY_SOURCE)
        msg = msg.split('\n')
        timestamp = int(msg[-1])

        if verbose:
            print('ID: {}\tMSG: {}'.format(self.rank, msg[:-1]))

        new_timestamp = max(self.clock, timestamp)
        if verbose:
            print('\tClock: {}\tTimestamp: {}\tNew: {}'\
                  .format(str(self.clock), str(timestamp), str(new_timestamp))
        self.clock = new_timestamp


    def send(self, msg, *, dest):
        msg = '{}\n{}'.format(msg, str(self.clock))
        MPI.COMM_WORLD.send(msg, dest=dest)


    def do_action(self, update='random',
                  action=lambda *args, **kwargs: time.sleep(0.5),
                  *args, **kwargs):
        msg = action(*args, **kwargs)
        self.clock += 1
        if update == 'random':
            dest = random.choice(self.universe)
        elif isinstance(update, int) and update in self.universe:
            dest = update
        else:
            return

        send(str(msg), dest=dest)
