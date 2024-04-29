class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_elements(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def sum_elements(self):
        current = self.head
        total = 0
        while current:
            try:
                total += float(current.data)
            except ValueError:
                pass
            current = current.next
        return total

    def average(self):
        current = self.head
        count = 0
        total = 0
        while current:
            try:
                total += float(current.data)
                count += 1
            except ValueError:
                pass
            current = current.next
        if count == 0:
            return 0
        else:
            return total / count

    def remove_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position is out of range")
                return
            current = current.next
        if current is None or current.next is None:
            print("Position is out of range")
            return
        current.next = current.next.next

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position is out of range")
                return
            current = current.next
        if current is None:
            print("Position is out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def add_list(self, new_list):
        for item in new_list:
            self.add_element(item)

    def remove_duplicates(self):
        current = self.head
        unique_values = set()
        previous = None
        while current:
            if current.data in unique_values:
                previous.next = current.next
            else:
                unique_values.add(current.data)
                previous = current
            current = current.next










