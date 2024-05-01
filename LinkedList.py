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

    def count_occurrences(self, value):
        count = 0
        index_list = []
        index = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
                index_list.append(index)
            current = current.next
            index += 1
        return count, index_list

    def remove_zeros(self):
        current = self.head
        while current and current.next:
            if current.next.data == 0:
                current.next = current.next.next
            else:
                current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def swap_adjacent_values(self):
        current = self.head
        while current and current.next:
            current.data, current.next.data = current.next.data, current.data
            current = current.next

    def remove_value(self, value):
        prev = None
        current = self.head
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                prev = current
                current = current.next

    def convert_to_list(self):
        return self.to_list()

    def reverse_pairs(self):
        current = self.head
        while current and current.next:
            current.data, current.next.data = current.next.data, current.data
            current = current.next.next


# Example usage:
linked_list = LinkedList()

# Add elements of different types
linked_list.add_element(1)
linked_list.add_element("two")
linked_list.add_element(True)
linked_list.add_element([4, 5, 6])
linked_list.add_element(0)
linked_list.add_element(False)
linked_list.add_element(3.14)

# Print linked list elements
print("Linked list elements:")
print(linked_list.to_list())

# Qiymatning takrorlanishini sanash
count, indices = linked_list.count_occurrences("two")
print(f"Number of occurrences of 'two': {count}")
print(f"Indices where 'two' occurs: {indices}")

# Nollarni olib tashlang
linked_list.add_element(0)
linked_list.add_element(0)
print("Linked list elements before removing zeros:")
print(linked_list.to_list())
linked_list.remove_zeros()
print("Linked list elements after removing zeros:")
print(linked_list.to_list())

# Bog'langan ro'yxatni ro'yxatga aylantiring
converted_list = linked_list.convert_to_list()
print("Converted list:")
print(converted_list)

# Qo'shni qiymatlarni almashtirish
linked_list.swap_adjacent_values()
print("Linked list elements after swapping adjacent values:")
print(linked_list.to_list())

# Muayyan qiymatni olib tashlang
linked_list.remove_value("two")
print("Linked list elements after removing 'two':")
print(linked_list.to_list())


# Convert linked list to list
converted_list = linked_list.convert_to_list()
print("Converted list after removal:")
print(converted_list)

# Teskari elementlar juftligi
linked_list.reverse_pairs()
print("Linked list elements after reversing pairs:")
print(linked_list.to_list())

