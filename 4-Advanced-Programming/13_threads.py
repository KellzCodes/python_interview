from threading import Lock, Thread
from time import sleep
import math

'''
create a thread
'''
# def run(content, delay=1):
#     sleep(delay)  # delay execution for a given number of seconds
#     print(content)

# thread1 = threading.Thread(target=run, args=("run1",1))
# thread2 = threading.Thread(target=run, args=("run2",2))
# thread1.start()  # outputs: run1
# print("Main Thread")
# thread1.join() # wait until the thread terminates
# thread2.start()  # outputs: run2

# # print the number of thread objects currrently alive
# print(threading.active_count())

# create a thread that will count to a specific number
# def print_values(values, delay):
#     for item in values:
#         print(item)
#         sleep(delay)

# thread3 = Thread(target=print_values, args=([1, 3, 5], 0.2))
# thread4 = Thread(target=print_values, args=([2, 4], 0.3))
# thread3.start()
# thread4.start()

'''
create a thread that will have a lock
'''
# def t1(lock):
#     print("starting t1")
#     lock.acquire()
#     sleep(1)
#     print("t1")
#     lock.release()

# def t2(lock):
#     print("starting t2")
#     lock.acquire()
#     sleep(1)
#     print("t2")
#     lock.release()

# lock = Lock()
# thread1 = Thread(target=t1, args=(lock, ))
# thread2 = Thread(target=t2, args=(lock, ))
# thread1.start()
# thread2.start()

'''
create a thread with two locks
'''
# def printing(values, start_lock, end_lock, name):
#     for item in values:
#         print(f"{name} waiting for lock")
#         start_lock.acquire()
#         print(item)
#         end_lock.release()

# lock1 = Lock()
# lock2 = Lock()
# lock2.acquire()

# thread1 = Thread(target=printing, args=([1, 3, 5], lock1, lock2, "t1"))
# thread2 = Thread(target=printing, args=([2, 4], lock2, lock1, "t2"))

# thread1.start()
# thread2.start()

'''
create a thread that needs prerequisites before it starts
'''
# def start_game(preq=[]):
#     print("Waiting to start game.")

#     for t in preq:
#         t.join()

#     print("Started Game!")

# def load_assets():
#     sleep(2)
#     print("loaded assets")

# def load_player():
#     sleep(1)
#     print("loaded player")

# load_assets_thread = Thread(target=load_assets)
# load_player_thread = Thread(target=load_player)
# preq = [load_player_thread, load_assets_thread]
# start_game_thread = Thread(target=start_game, args=(preq, ))

# load_player_thread.start()
# load_assets_thread.start()
# start_game_thread.start()

'''
Start, stop, and join the existing functions as threads in the program such that lst = [1, 4, 3, 5, 3] at the end of the 
program. You must use multithreading, create at least three threads and use both functions.
'''
# def append_values(lst, values=[], delay=1):
#     for value in values:
#         lst.append(value)
#         sleep(math.ceil(abs(delay)))
#
#
# def append_integer(lst, integer):
#     lst.append(integer)
#
#
# lst = []
# thread1 = threading.Thread(target=append_values, args=(lst, [1, 3, 5], 1))
# thread2 = threading.Thread(target=append_integer, args=(lst, 4))
# thread3 = threading.Thread(target=append_integer, args=(lst, 3))
# thread1.start()
# thread2.start()
# thread1.join()
# thread3.start()

'''
Write a program that uses multiple threads to gather the powers of two included in a range.

Your program must use at least 2 threads, each responsible for a portion of the range.

You are given a function called "is_power_of_two" to start with, which returns True if the given number is a power of two and False otherwise
'''


# RANGE_START = 0
# RANGE_END = 1000
#
# def is_power_of_two(x):
#     if x == 0:
#         return False
#     return (x & (x - 1)) == 0
#
# powers_of_two = set()
# set_lock = threading.Lock()
#
# def find_powers_of_two(iter):
#     for x in iter:
#         if is_power_of_two(x):
#             set_lock.acquire()
#             powers_of_two.add(x)
#             set_lock.release()
#
# thread1 = threading.Thread(target=find_powers_of_two, args=(range(RANGE_START, 250),))
# thread2 = threading.Thread(target=find_powers_of_two, args=(range(250, 500),))
# thread3 = threading.Thread(target=find_powers_of_two, args=(range(500, 750),))
# thread4 = threading.Thread(target=find_powers_of_two, args=(range(750, RANGE_END),))
#
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()

'''
Write a program that asks the user to input a positive integer "n" and uses multiple threads to print "foo" then "bar"
alternatively "n" times. Your program should print everything on the same line.

Your program must use at least "2" threads, one thread responsible for printing "foo" and another for printing "bar".

You may assume the input from the user for "n" will always be a positive integer.
'''
# def print_foo(n, foo_lock, bar_lock):
#     for _ in range(n):
#         foo_lock.acquire()
#         print("foo", end="")
#         bar_lock.release()
#
# def print_bar(n, foo_lock, bar_lock):
#     for _ in range(n):
#         bar_lock.acquire()
#         print("bar", end="")
#         foo_lock.release()
#
# n = int(input("Enter a positive integer: "))
#
# foo_lock = threading.Lock()
# bar_lock = threading.Lock()
# bar_lock.acquire()
#
# foo_thread = threading.Thread(target=print_foo, args=(n, foo_lock, bar_lock))
# bar_thread = threading.Thread(target=print_bar, args=(n, foo_lock, bar_lock))
#
# foo_thread.start()
# bar_thread.start()
#
# foo_thread.join()
# bar_thread.join()

