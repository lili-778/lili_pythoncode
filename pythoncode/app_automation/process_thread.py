import multiprocessing
import os
import sys
import threading
from time import sleep


def thread_demo(index):
    while True:
        print(f"thread_demo {index} pid={os.getpid()} thread_name={threading.current_thread().name}")
        sleep(1)


def process_demo(index):
    while True:
        print(f"process_demo {index} pid={os.getpid()} thread_name={threading.current_thread().name}")
        sleep(1)


def multi_thread(count):
    for index in range(count):
        thread = threading.Thread(target=thread_demo, args=[index])
        thread.start()
        sleep(1)


def multi_process(count):
    for index in range(count):
        process = multiprocessing.Process(target=process_demo, args=(index,))
        process.start()
        sleep(1)


if __name__ == '__main__':
    process_count = int(sys.argv[1])
    thread_count = int(sys.argv[2])
    multi_process(process_count)
    multi_thread(thread_count)
    input()

    