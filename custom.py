#!/usr/bin/env python3
import heapq
from collections import deque

class myQueue:
    def __init__(self):
        self.mode = ''
        self.priorty_queue = []
        self.stack = []
        self.queue = deque()

    def push(self, value):
        if self.mode == 'stack':
            return 1
        elif self.mode == 'queue':
            return 1
        elif self.mode == 'priority_queue':
            return 1
        else:
            return 0


    def pop(self):
        if (self.is_empty()):
            print("Error: Queue is empty")
            return 0
        else:
            if self.mode == 'stack':
                return 1 
            elif self.mode == 'queue':
                return 1
            elif self.mode == 'priority_queue':
                return 1
            else:
                return 0

    
    def is_empty(self):
        if self.mode == 'stack':
            return len(self.stack) == 0
        elif self.mode == 'queue':
            return len(self.queue) == 0
        elif self.mode == 'priority_queue':
            return len(self.priorty_queue) == 0
        else:
            return 0
        
    def print_queue(self):
        if self.mode == 'stack':
            print(self.stack)
        elif self.mode == 'queue':
            print(self.queue)
        elif self.mode == 'priority_queue':
            print(self.priorty_queue)
        else:
            return 0
        
def main():
    print("What do you want to use?")
    print("1. Stack")
    print("2. Queue")
    print("3. Priority Queue")
    print("4. Exit")
    mode = input("Enter your choice: ")
    queue = myQueue()
    if mode == '1':
        queue.mode = 'stack'
    elif mode == '2':
        queue.mode = 'queue'
    elif mode == '3':
        queue.mode = 'priority_queue'
    elif mode == '4':
        return 0
    else:
        print("Invalid choice")
        return 1

    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Check if empty")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            value = input("Enter the value: ")
            queue.push(value)
        elif choice == '2':
            queue.pop()
        elif choice == '3':
            print(queue.is_empty())
        elif choice == '4':
            break
        else:
            print("Invalid choice")
        
        print("Your current queue is: ")
        queue.print_queue()
    
    return 0

if __name__ == "__main__":
    main()

