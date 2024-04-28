from queue import Queue
from collections import deque

queue = Queue()
# to simulate application number
count = 0


def generate_request():
    # used global since goal is to show usage of queue and not keep code clean
    global count
    count += 1
    new_application = f'#{count}'
    queue.put(new_application)


def process_request():
    if not queue.empty():
        application = queue.get()
        print(application)
    else:
        print("Queue is empty")


def is_palindrome(word: str):
    if len(word.replace(' ', '')) <= 1:
        return True
    palindrome_deque = deque(word)
    left = palindrome_deque.popleft()
    right = palindrome_deque.pop()
    if left.lower() != right.lower():
        return False
    while len(palindrome_deque) > 1:
        if left == " ":
            left = palindrome_deque.popleft()
            continue
        if right == " ":
            right = palindrome_deque.popleft()
            continue
        left = palindrome_deque.popleft()
        right = palindrome_deque.pop()
        if left.lower() != right.lower():
            return False

    return True


def main():
    command = ""
    while command != "exit":
        generate_request()
        process_request()
        command = input()


if __name__ == '__main__':
    main()
