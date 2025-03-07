#!/usr/bin/env python3
'''
Problem #1 
Ellie Winter 

Implementing stack, queue and priority queue using a single class
'''

import heapq
from collections import deque


class my_queue:
    '''my_queue class that can be a stack, queue or priority queue'''
    def __init__(self):
        self.mode = ''
        self.priorty_queue = []
        self.stack = []
        self.queue = deque()

    def push(self, value):
        '''Push an element to the queue'''
        if self.mode == 'stack':
            self.stack.append(value)
        elif self.mode == 'queue':
            self.queue.appendleft(value)
        elif self.mode == 'priority_queue':
            heapq.heappush(self.priorty_queue, value)
        else:
            return 1
        return 0

    def pop(self):
        '''Pop an element from the queue'''
        if self.is_empty():
            print("Error: Queue is empty")
            return 0

        if self.mode == 'stack':
            self.stack.pop()
        elif self.mode == 'queue':
            self.queue.popleft()
        elif self.mode == 'priority_queue':
            heapq.heappop(self.priorty_queue)
        else:
            return 1
        return 0

    def is_empty(self):
        '''Check if the queue is empty'''
        if self.mode == 'stack':
            return len(self.stack) == 0
        if self.mode == 'queue':
            return len(self.queue) == 0
        if self.mode == 'priority_queue':
            return len(self.priorty_queue) == 0

        return 0

    def print_queue(self):
        '''Print the queue'''
        if self.mode == 'stack':
            print(self.stack)
        elif self.mode == 'queue':
            print(list(self.queue))
        elif self.mode == 'priority_queue':
            print(self.priorty_queue)
        return 0


def main():
    '''Main function'''
    print("What do you want to use?")
    print("1. Stack")
    print("2. Queue")
    print("3. Priority Queue")
    print("4. Exit")
    mode = input("Enter your choice: ")
    queue = my_queue()
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
        print("4. Confirm queue type")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            if queue.mode == 'priority_queue':
                priority = int(input("Enter the priority: "))
                while priority < 0:
                    print("Priority should be greater than or equal to 0")
                    priority = int(input("Enter the priority: "))
                value = input("Enter the value: ")
                queue.push((priority, value))
            else:
                value = input("Enter the value: ")
                queue.push(value)
        elif choice == '2':
            queue.pop()
        elif choice == '3':
            print(queue.is_empty())
        elif choice == '4':
            print(queue.mode)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

        print(f"Your current {queue.mode} is: ")
        queue.print_queue()

    return 0


if __name__ == "__main__":
    main()
