#!/usr/bin/env python3
'''
Problem #2
Ellie Winter 

Example:
Input:
    List 1: 2 -> 4 -> 3 (represents the number 342)
    List 2: 5 -> 6 -> 9 (represents the number 965)
Output:
    Result: 7 -> 0 -> 3->1 (represents the number 1307)
'''


class Node:
    '''Node class'''
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    '''Linked list class'''
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        '''Append a new node at the end of the linked list'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        '''Print the linked list'''
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')


def list_value(linked_list):
    '''
    Return the value of a linked list
    '''
    num = ''
    current_node = linked_list.head
    while current_node:
        num = str(current_node.data) + num
        current_node = current_node.next
    return int(num)


def add_lists(list1, list2):
    '''
    Add the value of two linked lists reversed and return
    the result in another linked list in reverse order
    '''
    num1 = list_value(list1)
    num2 = list_value(list2)

    result = str(int(num1) + int(num2))

    return result


def num_to_list(num):
    '''
    Convert a number to a linked list
    '''
    num = str(num)
    linked_list = LinkedList()
    while num != '':
        linked_list.append(num[-1])
        num = num[:-1]
    return linked_list


def main():
    '''Main function'''
    # initialize linked list 1
    list1 = LinkedList()
    list1.append(2)
    list1.append(4)
    list1.append(3)
    list1.print_list()

    # initialize linked list 2
    list2 = LinkedList()
    list2.append(5)
    list2.append(6)
    list2.append(9)
    list2.print_list()

    result_list = num_to_list(add_lists(list1, list2))

    print('Result:')
    result_list.print_list()


if __name__ == '__main__':
    main()
