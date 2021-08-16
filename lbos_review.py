from threading import Semaphore

# mutex
count = 0
mutex = Semaphore(1)

def mutex_thread():
    mutex.acquire()
    count += 1
    mutex.release()


# multiplex
count = 0
n = 5
mutex = Semaphore(n)

def multiplex_thread():
    mutex.acquire()
    count += 1
    mutex.release()

# rendezvous

a_arrived, b_arrived = Semaphore(0), Semaphore(0)

def rendezvous_thread_A():
    print("a1")
    a_arrived.release()
    b_arrived.acquire()
    print("a2")

def rendezvous_thread_B():
    print("b1")
    b_arrived.release()
    a_arrived.acquire()
    print("b2")

# barrier
n = 5
mutex = Semaphore(1)
barrier = Semaphore(0)
n_waiting = 0

def barrier_thread():
    print("before barrier")
    with mutex:
        n_waiting += 1
    if n_waiting == n:
        barrier.release()

    # turnstile
    barrier.acquire()
    barrier.release()
    print("after barrier")

# queue
def leader():
    pass