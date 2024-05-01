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


# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def add_element(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#
#     def display_elements(self):
#         current = self.head
#         while current:
#             print(current.data, end=" ")
#             current = current.next
#         print()
#
#     def sum_elements(self):
#         current = self.head
#         total = 0
#         while current:
#             try:
#                 total += float(current.data)
#             except ValueError:
#                 pass
#             current = current.next
#         return total
#
#     def average(self):
#         current = self.head
#         count = 0
#         total = 0
#         while current:
#             try:
#                 total += float(current.data)
#                 count += 1
#             except ValueError:
#                 pass
#             current = current.next
#         if count == 0:
#             return 0
#         else:
#             return total / count
#
#     def remove_at_position(self, position):
#         if position < 0:
#             print("Invalid position")
#             return
#         if position == 0:
#             self.head = self.head.next
#             return
#         current = self.head
#         for _ in range(position - 1):
#             if current is None:
#                 print("Position is out of range")
#                 return
#             current = current.next
#         if current is None or current.next is None:
#             print("Position is out of range")
#             return
#         current.next = current.next.next
#
#     def insert_at_position(self, data, position):
#         if position < 0:
#             print("Invalid position")
#             return
#         new_node = Node(data)
#         if position == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return
#         current = self.head
#         for _ in range(position - 1):
#             if current is None:
#                 print("Position is out of range")
#                 return
#             current = current.next
#         if current is None:
#             print("Position is out of range")
#             return
#         new_node.next = current.next
#         current.next = new_node
#
#     def add_list(self, new_list):
#         for item in new_list:
#             self.add_element(item)
#
#     def remove_duplicates(self):
#         current = self.head
#         unique_values = set()
#         previous = None
#         while current:
#             if current.data in unique_values:
#                 previous.next = current.next
#             else:
#                 unique_values.add(current.data)
#                 previous = current
#             current = current.next
#
#
#
#
#
#
#
#
#
#
