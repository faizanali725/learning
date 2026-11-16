
import time
import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)


def print_letters():
    for Char in "ABCDE":
        print(f"Letter: {Char}")
        time.sleep(1)



thread1 = threading.Thread(target = print_numbers)
thread2 = threading.Thread(target = print_letters)


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Finished printing numbers and letters.")



def greet(name):
    print(f"Hello, {name}!")


t = threading.Thread(target = greet, args = ("Alice",))
t.start()
t.join()