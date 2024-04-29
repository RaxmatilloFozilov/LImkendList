from LinkedList import LinkedList

ll = LinkedList()
ll.add_element(1)
ll.add_element(2)
ll.add_element(3)
ll.add_element(4)
ll.add_element(5)
ll.display_elements()

print("Sum of elements:", ll.sum_elements())
print("Average of elements:", ll.average())

ll.remove_at_position(2)
ll.display_elements()

ll.insert_at_position(3, 2)
ll.display_elements()

new_list = [3, 4, 5, 6, 7]
ll.add_list(new_list)
ll.display_elements()

ll.remove_duplicates()
ll.display_elements()



